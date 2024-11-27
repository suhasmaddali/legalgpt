import streamlit as st

# Page Configurations
st.set_page_config(page_title="Text-to-Image Artistry Studio", layout="wide")

# Sidebar for user inputs
with st.sidebar:
    st.markdown("👋 **Yo fam! Start here**")
    prompt = st.text_input("Enter prompt: start typing, Shakespeare ✍️", "An astronaut riding a rainbow unicorn, cinematic, dramatic")
    restrictions = st.text_input("Party poopers you don't want in the image? 🕵️‍♂️", "the absolute worst quality, distorted features")
    submit = st.button("Submit")

# Main content
st.markdown("# :rainbow[Text-to-Image Artistry Studio]")
st.markdown("Like what you see? Right-click and save! It's not stealing if we're sharing! 😏")

# Placeholder for the generated images
cols = st.columns(4)
for i, col in enumerate(cols):
    with col:
        st.image("https://via.placeholder.com/150", caption=f"Generated Image {i+1}")

# Resources Section
st.markdown("### Resources")
st.markdown("- [Stability AI SDXL Model on Replicate](https://replicate.com/stability-ai/sdxl)")

# Functionality when Submit button is pressed
if submit:
    st.success(f"Generating images based on your prompt: **{prompt}** and avoiding: **{restrictions}**")
