import streamlit as st
from transformers import GPT4

st.title("Change Management Post Generator")

# Input fields for user responses
synopsis = st.text_area("What is the primary goal or purpose of this change?")
summary = st.text_area("What specific functionalities or features are being added or modified in this change?")
implementation_plan = st.text_area("What are the step-by-step actions required to implement this change?")
rollback_plan = st.text_area("What steps should be taken to revert to the previous state if the change fails?")
severity = st.selectbox("On a scale of 1 to 5, how critical is this change?", [1, 2, 3, 4, 5])
risks = st.text_area("What are the potential risks involved?")

if st.button("Generate Post"):
    # Example of combining user inputs into a structured post
    post = f"""
    ## Deployment Change Management Post

    **Synopsis:**
    {synopsis}

    **Summary of Changes:**
    {summary}

    **Implementation Plan:**
    {implementation_plan}

    **Rollback Plan:**
    {rollback_plan}

    **Severity and Risks:**
    Severity: {severity}/5
    Risks: {risks}
    """
    
    st.subheader("Generated Change Management Post")
    st.write(post)
    st.download_button("Download as PDF", post, file_name="change_management_post.pdf")

