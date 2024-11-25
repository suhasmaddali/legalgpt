import streamlit as st
import pandas as pd
import os

# File to save the data
DATA_FILE = "legal_issues_data.csv"

# Set page title
st.set_page_config(page_title="Legal Issue Enquiry", layout="centered")

# Title of the app
st.title("Describe your legal issue")

# Initialize the data file if it doesn't exist
if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=[
        "Country", "Help On Behalf Of", "Legal Issue", "Budget Range", 
        "Description", "Full Name", "Email"
    ])
    df.to_csv(DATA_FILE, index=False)

# Dropdown: Select the country
countries = ["Aruba", "United States", "Canada", "India", "United Kingdom", "Australia"]
country = st.selectbox("Select the country where legal assistance is required*", countries)

# Radio Buttons: Help on behalf of
help_on_behalf_of = st.radio(
    "I'm looking for help on behalf of:",
    ["myself", "a business/company"]
)

# Dropdown: Legal issue relates to
legal_issues = ["Issue 1", "Issue 2", "Issue 3", "Other"]
legal_issue = st.selectbox("My legal issue relates to:*", legal_issues)

# Slider: Budget range
budget = st.slider("My budget range is ($):", 0, 5000, 0)

# Text area: Description of legal matter
description = st.text_area("Outline your legal matter and include key questions:")

# Input fields: Name and email
col1, col2 = st.columns(2)
with col1:
    full_name = st.text_input("Your name *")
with col2:
    email = st.text_input("Email address *")

# Submit button
if st.button("SUBMIT YOUR ENQUIRY"):
    if full_name and email and legal_issue:
        # Append data to the file
        new_entry = pd.DataFrame([{
            "Country": country,
            "Help On Behalf Of": help_on_behalf_of,
            "Legal Issue": legal_issue,
            "Budget Range": budget,
            "Description": description,
            "Full Name": full_name,
            "Email": email
        }])
        new_entry.to_csv(DATA_FILE, mode="a", index=False, header=False)
        st.success("Your enquiry has been submitted successfully.")
    else:
        st.error("Please fill all required fields.")

# Display saved entries
st.markdown("---")
st.write("### Submitted Enquiries")
if os.path.exists(DATA_FILE):
    saved_data = pd.read_csv(DATA_FILE)
    st.dataframe(saved_data)
else:
    st.write("No data available.")
