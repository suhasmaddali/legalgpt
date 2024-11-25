import streamlit as st
from io import BytesIO

# Page Configuration
st.set_page_config(
    page_title="Analyze Media - Tenant-Landlord Legal AI Suite",
    page_icon="📂",
    layout="wide",
)

# Title and Introduction
st.title("📂 Analyze Media")
st.subheader("Upload and Analyze Media Files")
st.markdown(
    """
    Use this tool to upload media files for analysis. The AI suite will process the file and provide actionable insights relevant to tenant-landlord legal disputes.
    """
)

# Upload Section
st.header("📤 Upload Your Media File")
st.markdown(
    """
    Supported file types:
    - **Text files** (.txt, .pdf): Extract legal content for analysis.
    - **Audio files** (.mp3, .wav): Transcribe and analyze conversations or legal statements.
    - **Video files** (.mp4, .avi): Extract audio for transcription and legal insights.
    """
)

uploaded_file = st.file_uploader(
    "Drag and drop your file here, or click to upload",
    type=["txt", "pdf", "mp3", "wav", "mp4", "avi"],
    accept_multiple_files=False,
)

# Process Uploaded File
if uploaded_file is not None:
    st.success("File uploaded successfully!")
    file_details = {
        "Filename": uploaded_file.name,
        "File Type": uploaded_file.type,
        "File Size (KB)": round(len(uploaded_file.read()) / 1024, 2),
    }

    st.write("### File Details:")
    st.json(file_details)

    # Reset the file pointer
    uploaded_file.seek(0)

    # Extract and Display Content Based on File Type
    if uploaded_file.type in ["text/plain", "application/pdf"]:
        st.write("### Extracted Text Content:")
        try:
            content = uploaded_file.read().decode("utf-8")
            st.text(content[:1000])  # Display the first 1000 characters
        except Exception as e:
            st.error(f"Unable to read the file. Error: {e}")

    elif uploaded_file.type in ["audio/mpeg", "audio/wav", "video/mp4", "video/x-msvideo"]:
        st.write("### Media Analysis (Audio/Video):")
        st.info(
            """
            **Transcription** and **legal insights** will be generated using AI tools like OpenAI or Assembly AI.
            (Integrate transcription logic here based on your subscriptions and API access.)
            """
        )
        # Example Placeholder: Save the file for later processing
        with open(f"temp_{uploaded_file.name}", "wb") as f:
            f.write(uploaded_file.read())
        st.success("Media file saved for further processing.")

# Example Placeholder: AI Integration
st.header("🤖 AI Analysis Output (Example Placeholder)")
st.markdown(
    """
    Integrate your AI model here to process the uploaded file and provide actionable insights.

    **Example**:
    - For text files: Highlight legal clauses, tenant-landlord disputes, or actionable points.
    - For audio/video files: Provide a transcription and analyze the content for legal relevance.
    """
)
st.code(
    """
    from openai_api import transcribe_audio, analyze_text

    # Example transcription
    transcription = transcribe_audio(uploaded_file)
    insights = analyze_text(transcription)

    st.write("### Transcription:")
    st.text(transcription)

    st.write("### Legal Insights:")
    st.write(insights)
    """,
    language="python",
)

# Footer
st.markdown("---")
st.markdown("🚀 Built with ❤️ using **Streamlit** | Empowering Legal Tech with AI")
