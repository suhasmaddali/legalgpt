import streamlit as st
import pandas as pd
import plotly.express as px
import os

# File to save feedback data
FEEDBACK_FILE = "feedback_data.csv"

# Set page title
st.set_page_config(page_title="Feedback Form")

# Title of the feedback form
st.title("We Value Your Feedback")

# Content list for the dropdown
content_list = [
    "Home", "Disclaimer", "Transcript", "Chat", "Search", 
    "Court Certified Transcript", "Investigation Aid", 
    "Lease Agreement Summarizer V2", "Spectrograph", 
    "Analyze Media", "Analyze Speech", "Diagnose Audio", 
    "Feedback", "Audio Recording Laws", "About JurisVoiceGPT", 
    "Submit a Request", "Case Submission", "Knowledge Graph", 
    "Legal Info Videos", "Maps"
]

# Status options for feedback
status_options = ['New', 'In Progress', 'Testing', 'User Accepted', 'Implemented Successfully', 'Closed']

# Load feedback data from file or create default examples
if os.path.exists(FEEDBACK_FILE):
    feedback_data = pd.read_csv(FEEDBACK_FILE)
else:
    # Create example feedback data
    feedback_data = pd.DataFrame({
        'Page': ["Home", "Chat", "Search", "Feedback", "Case Submission"],
        'Feedback': [
            "The homepage design is intuitive and easy to navigate.",
            "Chat responses are fast but sometimes inaccurate.",
            "Search functionality needs improvement in filtering results.",
            "Feedback section could have more detailed instructions.",
            "Case submission form is user-friendly, but confirmation emails are delayed."
        ],
        'Status': ["New", "In Progress", "Testing", "User Accepted", "Implemented Successfully"]
    })
    # Save initial example data to file
    feedback_data.to_csv(FEEDBACK_FILE, index=False)

# Instructions
st.write("Please select a page and provide your feedback. You can add multiple entries as needed.")

# Dropdown to select the page
selected_page = st.selectbox("Select a Page:", content_list)

# Text area for feedback
feedback_text = st.text_area("Enter your Feedback:")

# Submit button
if st.button("Submit Feedback"):
    if feedback_text.strip():
        # Append new feedback entry
        new_entry = pd.DataFrame({
            'Page': [selected_page],
            'Feedback': [feedback_text],
            'Status': ['New']  # Default status is 'New'
        })
        feedback_data = pd.concat([feedback_data, new_entry], ignore_index=True)
        feedback_data.to_csv(FEEDBACK_FILE, index=False)  # Save to file
        st.success("Your feedback has been submitted and saved.")
    else:
        st.error("Feedback cannot be empty.")

# Display the feedback data
st.write("### Current Feedback Entries:")
if not feedback_data.empty:
    # Editable DataFrame for status updates
    editable_data = st.data_editor(
        feedback_data,
        key="feedback_editor",
        column_config={
            'Status': st.column_config.SelectboxColumn(
                "Status",
                options=status_options,
                default="New"
            )
        },
        use_container_width=True
    )
    # Save updates back to the file when edited
    feedback_data.update(editable_data)
    feedback_data.to_csv(FEEDBACK_FILE, index=False)
else:
    st.write("No feedback entries available.")

# Display summary graph
if not feedback_data.empty:
    st.write("### Feedback Progress Summary:")
    status_counts = feedback_data['Status'].value_counts().reset_index()
    status_counts.columns = ['Status', 'Count']
    fig = px.bar(status_counts, x='Status', y='Count', title='Feedback Status Distribution')
    st.plotly_chart(fig)
else:
    st.write("No feedback entries to display.")
