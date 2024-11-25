import streamlit as st

# Create a dictionary for username and password
credentials = {
    "admin": "password123",
    "user1": "mypassword",
    "guest": "guest123"
}

# Define a function for the login page
def login():
    st.title("Login to JurisVoiceGPT")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username in credentials and credentials[username] == password:
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.success(f"Welcome, {username}! Please click login button once again. Thank you")
        else:
            st.error("Invalid username or password. Please try again.")

# Initialize session state for login
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# Display the login page if not logged in
if not st.session_state["logged_in"]:
    login()
else:
    # Define the pages
    pages = [
        st.Page("views/home.py", title="Home", icon="🏠"),
        st.Page("views/disclaimer.py", title="Disclaimer", icon="📜"),
        st.Page("views/transcript.py", title="Transcript", icon="📜"),
        st.Page("views/chat.py", title="Chat", icon="💬"),
        st.Page("views/search.py", title="Search", icon="🔍"),
        st.Page("views/court_certified_transcript.py", title="Court Certified Transcript", icon="⚖️"),
        st.Page("views/investigation_aid.py", title="Investigation Aid", icon="🕵️"),
        st.Page("views/lease_agreement_summarizer_v2.py", title="Lease Agreement Summarizer V2", icon="📄"),
        st.Page("views/spectrograph.py", title="Spectrograph", icon="🔉"),
        st.Page("views/analyze_media.py", title="Analyze Media", icon="🔬"),
        st.Page("views/analyze_speech.py", title="Analyze Speech", icon="🔬"),
        st.Page("views/diagnose_audio.py", title="Diagnose Audio", icon="🧪"),
        st.Page("views/feedback.py", title="Feedback", icon="✍️"),
        st.Page("views/audio_recording_laws.py", title="Audio Recording Laws", icon="🔊"),
        st.Page("views/about_jurisvoiceGPT.py", title="About JurisVoiceGPT", icon="ℹ️"),
        st.Page("views/submit_a_request.py", title="Submit a Request", icon="✍️"),
        st.Page("views/case_submission.py", title="Case Submission", icon="📜"),
        st.Page("views/knowledge_graph.py", title="Knowledge Graph", icon="📈"),
        st.Page("views/legal_info_videos.py", title="Legal Info Videos", icon="ℹ️"),
        st.Page("views/maps.py", title="Maps", icon="🔬")
    ]

    # Configure navigation
    current_page = st.navigation(pages)
    current_page.run()









        
        




