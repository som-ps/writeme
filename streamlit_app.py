import streamlit as st
import openai

# Directly set the OpenAI API key
openai.api_key = "sk-proj-8YP3eebcyurJI5TQZ9xAT3BlbkFJcSwZeG4Vc4cixShKIKaM"

st.title("Change Management Post Generator")

st.header("Step 1: Provide Details for Change Management Post")

# Input fields for user responses
synopsis = st.text_area("What is the primary goal or purpose of this change?")
summary = st.text_area("What specific functionalities or features are being added or modified in this change?")
implementation_plan = st.text_area("What are the step-by-step actions required to implement this change?")
rollback_plan = st.text_area("What steps should be taken to revert to the previous state if the change fails?")
severity = st.selectbox("On a scale of 1 to 5, how critical is this change?", [1, 2, 3, 4, 5])
risks = st.text_area("What are the potential risks involved?")

if st.button("Generate Post"):
    # Combine inputs into a prompt for OpenAI API
    prompt = f"""
    Create a professional change management post with the following details:

    Synopsis:
    {synopsis}

    Summary of Changes:
    {summary}

    Implementation Plan:
    {implementation_plan}

    Rollback Plan:
    {rollback_plan}

    Severity and Risks:
    Severity: {severity}/5
    Risks: {risks}
    """

    # Call OpenAI API to generate the post
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7,
    )

    post = response.choices[0].text.strip()

    st.subheader("Generated Change Management Post")
    st.write(post)

    # Download button for the generated post
    st.download_button("Download as Text", post, file_name="change_management_post.txt")

st.header("Step 2: Review and Edit (Optional)")
edited_post = st.text_area("Edit the generated post if needed:", "", height=300)

if st.button("Download Edited Post"):
    st.download_button("Download as Text", edited_post, file_name="edited_change_management_post.txt")
