import streamlit as st
from pathlib import Path

# Set page title
st.set_page_config(page_title="Court PDF Download", layout="centered")

# Title of the app
st.title("Court PDF Download")

# Example list of PDF files (use placeholders or actual file paths)
pdf_files = [
    {"name": "Court Transcript 1", "path": "example_pdf_1.pdf"},
    {"name": "Court Transcript 2", "path": "example_pdf_2.pdf"},
    {"name": "Legal Document 1", "path": "example_pdf_3.pdf"},
    {"name": "Legal Document 2", "path": "example_pdf_4.pdf"},
]

# Function to check if the PDF exists
def check_file_exists(file_path):
    return Path(file_path).exists()

# Display PDF download icons
if pdf_files:
    for pdf in pdf_files:
        col1, col2 = st.columns([1, 8])
        with col1:
            st.image("https://upload.wikimedia.org/wikipedia/commons/8/87/PDF_file_icon.svg", width=50)
        with col2:
            if check_file_exists(pdf["path"]):
                st.markdown(f"[{pdf['name']}]({pdf['path']})")  # Link to download the PDF
            else:
                st.write(f"{pdf['name']} (Not available for download)")
else:
    st.write("No PDFs available for download.")

# Footer or additional content
st.markdown("---")
st.write("This is a POC to demonstrate displaying multiple PDFs for download.")
