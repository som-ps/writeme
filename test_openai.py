import openai

# Directly set the OpenAI API key
openai.api_key = "sk-proj-8YP3eebcyurJI5TQZ9xAT3BlbkFJcSwZeG4Vc4cixShKIKaM"

try:
    # Call OpenAI API to generate a simple completion
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Say hello to the world.",
        max_tokens=5,
    )
    print(response.choices[0].text.strip())

except Exception as e:
    print(f"An error occurred: {e}")
