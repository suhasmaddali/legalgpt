import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Tenant-Landlord Legal AI Suite",
    page_icon="🤖",
    layout="wide",
)

# Title and Introduction
st.title("🏠 Tenant-Landlord Legal AI Suite")
st.subheader("Empowering Tenants and Landlords Through AI")
st.markdown(
    """
    Welcome to the **Tenant-Landlord Legal AI Suite**, an innovative product designed to address tenant-landlord disputes efficiently.
    Our AI-driven solution leverages cutting-edge technology to offer tools for legal support, data processing, and actionable insights.
    """
)

# Section: About the Product
st.header("📄 About the Product")
st.markdown(
    """
    The product is a **Proof of Concept (PoC)** designed to help:
    - **Tenants** sue landlords for legal disputes.
    - **Landlords** pursue legal action against tenants (future version).

    The PoC utilizes advanced **AI tools** to process extensive legal data, making it faster and more reliable than traditional methods.
    """
)
st.markdown(
    """
    ### Current Development Needs:
    - A **user-friendly interface (UI)** to ensure accessibility and ease of use.
    - **Backend support** to handle scaling and API integration for high demand.
    """
)

# Section: Challenges and Opportunities
st.header("🚀 Challenges & Opportunities")

st.subheader("Challenges")
st.markdown(
    """
    - Limited **developer support** for scaling and feature enhancement.
    - Absence of a **dedicated front-end developer** to create a seamless UI.
    - The project is **self-funded**, with financial constraints in hiring full-time resources.
    """
)

st.subheader("Opportunities")
st.markdown(
    """
    - **Investor Interest**: Morgan Stanley's startup financing division has shown interest in investing $250K.
    - **Market Expansion**: The product can be tailored for landlords, creating a broader market reach.
    - **AI Showcase**: This product can position itself as a **flagship AI project**, demonstrating the potential of AI in legal tech.
    """
)

# Section: Collaboration Needs and Goals
st.header("🤝 Collaboration & Strategic Goals")
st.markdown(
    """
    ### Collaboration Needs:
    - **Front-End Development**: Expertise in building intuitive, world-class interfaces.
    - **Backend Support**: Proficiency in scaling infrastructure, integrating APIs, and deploying applications.

    ### Strategic Goals:
    - Integrate the product under **Dana** or an enterprise co-developed by **Venu and the team**.
    - Showcase the product as a **flagship AI initiative** to attract clients, partners, and investors.
    - Create a portfolio of **legal AI solutions** for diverse use cases.
    """
)

# Section: Technology Stack
st.header("🧠 AI Tools and Technology Stack")
st.markdown(
    """
    The product is powered by premium AI tools, ensuring high-quality performance:
    - **OpenAI GPT Models**: For natural language understanding and legal document summarization.
    - **Claude**: For advanced legal analysis and nuanced interpretation of data.
    - **Assembly AI**: For transcription and audio data processing.

    API keys and premium subscriptions are ready for integration and testing.
    """
)

# Section: Product Vision
st.header("🌟 Product Vision")
st.markdown(
    """
    Our vision is to democratize legal support by offering AI-driven tools that simplify complex disputes. 
    With scalable solutions for tenants and landlords, we aim to set a benchmark in legal tech innovation.
    """
)
st.markdown(
    """
    **Key Highlights:**
    - Cost-effective and accessible legal support.
    - User-friendly design with AI-powered analytics.
    - Potential for real-time legal insights and multi-user collaboration.
    """
)

# Section: Call to Action
st.header("📢 Join the Journey")
st.markdown(
    """
    We are looking for passionate **developers** and **investors** to join us in this transformative journey.

    ### Why Collaborate?
    - **Developers**: Contribute to building a scalable, intuitive solution that impacts the legal tech space.
    - **Investors**: Be part of a product with proven interest and high growth potential.

    Let’s innovate and make legal assistance accessible for everyone.
    """
)

# Contact Information
st.header("📬 Contact Information")
st.markdown(
    """
    - **Founder**: Dana
    - **Email**: [example@example.com](mailto:example@example.com)
    - **API Access**: Available for integration and testing.
    """
)

# Footer
st.markdown("---")
st.markdown(
    """
    🚀 Built with ❤️ using **Streamlit** |
    Transforming Legal Tech Through AI Innovation.
    """
)

# Embedding Images
st.header("📸 Visual Insights")
st.markdown(
    """
    Below are some visuals representing tenant-landlord legal scenarios:
    """
)

# Image 1: Landlord-Tenant Agreement
st.image(
    "https://images.pexels.com/photos/8292795/pexels-photo-8292795.jpeg",
    caption="Landlord-Tenant Agreement",
    use_container_width=True
)

# Image 2: Legal Consultation
st.image(
    "https://images.pexels.com/photos/5673502/pexels-photo-5673502.jpeg",
    caption="Legal Consultation",
    use_container_width=True
)

# Image 3: Signing Contract
st.image(
    "https://images.pexels.com/photos/5673488/pexels-photo-5673488.jpeg",
    caption="Signing Contract",
    use_container_width=True
)
