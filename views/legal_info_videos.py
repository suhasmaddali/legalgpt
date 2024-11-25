import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI

# Page Configuration
st.set_page_config(
    page_title="Georgia Tenant and Landlord Laws Chatbot",
    page_icon="🤖",
    layout="wide",
)

# Initialize OpenAI Client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Initialize Session States
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

if "system_message_set" not in st.session_state:
    st.session_state.system_message_set = False

# Title of the app
st.title("Georgia Tenant and Landlord Laws: Legal GPT Chatbot")

# Description of the app
st.markdown(
    """
    This application provides insights into Georgia's tenant and landlord laws using the transcripts of curated videos.
    Ask questions, and the chatbot will analyze the transcripts to provide relevant answers, leveraging "Legal GPT."
    """
)

# List of YouTube video links related to the topic
videos = [
    {
        "title": "The Ultimate Guide to Georgia Landlord Tenant Laws & Rights",
        "url": "https://www.youtube.com/watch?v=i-LxPeSvcRc",
        "id": "i-LxPeSvcRc",
    },
    {
        "title": "Georgia Tenant Landlord Laws",
        "url": "https://www.youtube.com/watch?v=bqc-7hU9Zag",
        "id": "bqc-7hU9Zag",
    },
    {
        "title": "Georgia Landlord Tenant Laws | American Landlord",
        "url": "https://www.youtube.com/watch?v=eWr1DrekFWk",
        "id": "eWr1DrekFWk",
    },
    {
        "title": "Lease & Landlord-Tenant Laws in Georgia",
        "url": "https://www.youtube.com/watch?v=eqaXikqR-Fs",
        "id": "eqaXikqR-Fs",
    },
    {
        "title": "New Georgia law giving renters greater protections now in effect",
        "url": "https://www.youtube.com/watch?v=_1Na1mK6njs",
        "id": "_1Na1mK6njs",
    },
]

# Function to fetch transcripts for all videos
@st.cache_data
def fetch_transcripts(video_ids):
    transcripts = {}
    for video_id in video_ids:
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            full_text = " ".join([entry["text"] for entry in transcript])
            transcripts[video_id] = full_text
        except Exception as e:
            transcripts[video_id] = f"Transcript not available: {str(e)}"
    return transcripts


# Fetch transcripts for all videos
video_ids = [video["id"] for video in videos]
transcripts = fetch_transcripts(video_ids)

# Combine all transcripts
combined_transcripts = "\n".join([transcripts[video_id] for video_id in video_ids if video_id in transcripts])

# Display video list
st.header("🎥 Informative Videos")
for video in videos:
    st.subheader(video["title"])
    st.video(video["url"])

# Chatbot Section
st.header("💬 Legal GPT Chatbot")
st.markdown(
    """
    Ask any question related to Georgia tenant and landlord laws based on the video transcripts.
    """
)

# Define the Legal GPT system message
system_message_legal = """
Product Description:
This is a legal tech product designed to assist tenants in suing landlords, with the potential for a landlord-oriented version. The PoC needs UI enhancements and modifications for scalability, utilizing premium subscriptions to OpenAI, Claude, and Assembly AI for data processing.

Financial and Investment Background:
Funding has been self-supported. An investor expressed interest in investing $250K, but it was declined due to lack of developer support.

Developer Requirements:
Seeking coding expertise, particularly in front-end development, to assist with product scaling and enhancement.

Partnership and Collaboration:
Fully vested with Dana, aiming to integrate the product under Dana’s umbrella for strategic alignment with ongoing projects involving Venu.

Long-Term Strategy:
The product launch aims to showcase AI capabilities for pitching contracts and demonstrating solution viability without immediate revenue focus.

NEVER answer anything outside the legal documents and legal information.
"""

if not st.session_state.system_message_set:
    st.session_state.messages.append({"role": "system", "content": system_message_legal})
    st.session_state.system_message_set = True

# Display previous chat messages
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Handle user input and LLM response
if prompt := st.chat_input("Ask your legal question here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepare LLM request messages
    assistant_prompt = f"""
    You are an AI legal assistant. Provide legal guidance based strictly on the context of tenant-landlord laws, documents, and agreements.
    Below are the combined transcripts of the videos, which you must use to provide answers:
    {combined_transcripts}
    
    User Question: {prompt}
    """

    # Call OpenAI API
    with st.chat_message("assistant"):
        try:
            response = client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": "system", "content": system_message_legal},
                    {"role": "user", "content": f"Combined transcripts: {combined_transcripts}"},
                    {"role": "user", "content": f"Question: {prompt}"}
                ],
                stream=True,
            )
            response_content = st.write_stream(response)
            st.session_state.messages.append({"role": "assistant", "content": response_content})
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# Footer
st.markdown("---")
st.markdown(
    "**Disclaimer:** The responses are based on the transcripts of videos provided for informational purposes only and should not be considered legal advice."
)

