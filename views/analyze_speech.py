import streamlit as st
from streamlit_mic_recorder import mic_recorder
from openai import OpenAI
from gtts import gTTS
import tempfile
import os
import base64

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("Record your situtation")
# Streamlit app title
st.markdown("Record your problem and I will give authentic legal advise.")

# Initialize session state
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to transcribe audio
def transcribe_audio(client, audio_path):
    with open(audio_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    return transcript.text

# Function to convert text to speech and play it
def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio_file:
        tts.save(temp_audio_file.name)
        temp_audio_path = temp_audio_file.name

    # Read the audio file and encode it to base64
    with open(temp_audio_path, "rb") as audio_file:
        audio_bytes = audio_file.read()
        audio_base64 = base64.b64encode(audio_bytes).decode()

    # Create an audio HTML element with autoplay
    audio_html = f"""
    <audio autoplay="true" controls="controls" style="display:none;">
        <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3" />
    </audio>
    """
    st.markdown(audio_html, unsafe_allow_html=True)

    # Clean up temporary file
    os.remove(temp_audio_path)

audio = mic_recorder()

if audio:
    # Save the recorded audio to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio_file:
        temp_audio_file.write(audio['bytes'])
        temp_audio_path = temp_audio_file.name

    st.audio(temp_audio_path, format="audio/wav")

    # Automatically transcribe audio and interact with the LLM
    try:
        transcription = transcribe_audio(client, temp_audio_path)
        
        # Add the transcription as a user message
        additional_message = "Give tips based on this conversation with landlord and tenant to save their time and money"
        enhanced_prompt = transcription + " " + additional_message
        # st.session_state.messages.append({"role": "user", "content": transcription})
        st.session_state.messages.append({"role": "user", "content": enhanced_prompt})
        
        # Get the assistant's response
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
        
        text_to_speech(response)

        # Add the assistant's response to the chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

    except Exception as e:
        st.error(f"An error occurred during transcription or response generation: {e}")

    # Clean up temporary file
    os.remove(temp_audio_path)

