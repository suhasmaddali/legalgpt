import streamlit as st

# Set page title
st.set_page_config(page_title="Submit a Request", layout="centered")

# Page header
st.title("Submit a Request")

# Email Address
email = st.text_input("Your email address", placeholder="Enter your email address")

# Subject
subject = st.text_input("Subject", placeholder="Enter the subject of your request")

# Type of Problem (Dropdown)
problem_type = st.selectbox("Type of Problem", ["Report Content", "Technical Issue", "Billing Inquiry", "Other"])

# Description
description = st.text_area("Description", placeholder="Please enter the details of your request...")

# Attachment (File uploader)
attachment = st.file_uploader("Attachment (optional)", type=["png", "jpg", "jpeg", "pdf", "docx", "xlsx"], help="Limit 500MB per file")

# Submit Button
if st.button("Submit"):
    if email and subject and description:
        st.success("Your request has been submitted successfully!")
    else:
        st.error("Please fill in all required fields before submitting.")

