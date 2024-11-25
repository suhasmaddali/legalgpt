import streamlit as st
import pandas as pd
import random

# Function to generate 20,000 transcript records
@st.cache_data
def generate_transcripts(num_records=20000):
    actions = [
        "The tenant is required to",
        "The landlord must ensure",
        "The tenant has the right to",
        "The landlord may initiate",
        "Both parties must adhere to",
        "The tenant must provide",
        "The landlord must return",
        "The tenant has the right to privacy",
        "The landlord cannot discriminate",
        "The tenant may withhold rent",
        "The landlord must provide written notice",
        "The tenant must not cause damage",
        "The landlord must comply with",
        "The tenant can seek legal advice if",
        "The landlord must resolve disputes by",
        "The tenant has the option to",
        "The landlord must repair",
        "The tenant is entitled to",
        "The landlord should inform tenants about",
        "Both parties can agree to"
    ]
    topics = [
        "pay rent on time", "ensure the property is habitable", 
        "request essential repairs", "eviction for lease violation", 
        "state and federal housing laws", "written notice before vacating",
        "security deposit policies", "advance notice before entry",
        "discrimination laws", "delayed rent adjustments", 
        "damages caused by tenants", "privacy and access rights",
        "building codes and regulations", "legal rights and protections", 
        "alternative dispute resolutions", "amend rental agreements",
        "maintenance obligations", "tenant safety measures",
        "utility and bill responsibilities", "lease terminations and renewals"
    ]

    transcripts = []
    for i in range(1, num_records + 1):
        transcripts.append({
            "Index": i,
            "Start Time": f"00:{i // 60:02}:{i % 60:02}",
            "End Time": f"00:{(i // 60):02}:{(i % 60 + 5):02}",
            "Transcript": f"{random.choice(actions)} {random.choice(topics)}."
        })
    return pd.DataFrame(transcripts)

# Load or generate the transcript data
transcript_df = generate_transcripts()

# Title of the Streamlit App
st.title("Transcript Search")

# Search bar for filtering transcripts
query = st.text_input("Search for a specific term or phrase:")

# Filter the transcript based on the search query
if query:
    filtered_df = transcript_df[transcript_df["Transcript"].str.contains(query, case=False, na=False)]
else:
    filtered_df = transcript_df

# Display the filtered results in a table
st.dataframe(filtered_df, use_container_width=True)

# Footer (optional)
st.markdown("---")
st.markdown("**Note:** Use the search bar above to filter transcript records by keywords or phrases.")
