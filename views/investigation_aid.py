import streamlit as st
from PyPDF2 import PdfReader
from openai import OpenAI
import base64
from io import BytesIO
import os

# Page Configuration
st.set_page_config(
    page_title="Legal GPT with PDF Analysis",
    page_icon="📄",
    layout="wide",
)

openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

# Initialize Session States
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

if "uploaded_pdf_text" not in st.session_state:
    st.session_state.uploaded_pdf_text = ""

# Function to display PDF in Streamlit
def show_pdf(file):
    base64_pdf = base64.b64encode(file).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# Function to extract text from PDF
def extract_text_from_pdf(file):
    reader = PdfReader(BytesIO(file))
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# LLM Insights Based on Uploaded PDF
def analyze_pdf_with_llm(pdf_text, question):
    # Prepare the system message with context
    system_message = f"""
    You are a legal assistant specialized in providing insights based on legal documents. Use the uploaded PDF content to answer questions. 
    Always base your response on the provided text and avoid assumptions.
    
    {question}
    """
    
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": f"The document text is: {pdf_text}"},
        {"role": "user", "content": f"Question: {question}"}
    ]

    # Call OpenAI API
    response = client.chat.completions.create(
        model=st.session_state["openai_model"],
        messages=messages,
        stream=False,
    )
    return response["choices"][0]["message"]["content"]

# Title and Introduction
st.title("📄 Legal GPT with PDF Analysis")
st.markdown(
    """
    Welcome to **Legal GPT**. Upload a legal document (PDF), and ask questions to gain insights based on its content. 
    """
)

# PDF Upload Section
st.header("📤 Upload Your PDF Document")
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file:
    # Extract and display the PDF text
    pdf_file = uploaded_file.read()
    pdf_text = extract_text_from_pdf(pdf_file)
    st.session_state.uploaded_pdf_text = pdf_text
    
    st.header("📄 Preview Document")
    show_pdf(pdf_file)

    # Styled Section
    st.markdown(
        """
        <div style="background-color:#f0f8ff; padding:15px; border-radius:10px;">
            <h2 style="color:#1f618d; text-align:center;">🔍 Analyze Legal Document</h2>
            <p style="color:#34495e; text-align:center; font-size:18px; font-weight:bold;">
                This section is integrated with LLM to analyze your uploaded legal document.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    system_message_legal = f"""
    You are an AI legal assistant. Provide legal guidance based strictly on the context of tenant-landlord laws, documents, and agreements.
    Avoid giving advice outside this domain.

    {pdf_text}
    """

    if "system_message_set" not in st.session_state:
        st.session_state.messages.append({
            'role': 'system',
            'content': system_message_legal
        })
        st.session_state.system_message_set = True

    for message in st.session_state.messages:
        if message["role"] != "system":
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    if prompt := st.chat_input("Ask a legal question:"):
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
            response_content = st.write_stream(stream)

        st.session_state.messages.append({"role": "assistant", "content": response_content})
