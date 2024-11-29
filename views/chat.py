from openai import OpenAI
import streamlit as st
import os

st.title("Legal GPT")

openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

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

st.session_state.messages.append({
    'role': 'system',
    'content': system_message_legal
})
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})