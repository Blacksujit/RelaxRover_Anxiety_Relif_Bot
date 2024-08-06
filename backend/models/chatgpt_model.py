import openai


# Set your OpenAI API key
openai.api_key = 'OPEN_AI_API_KEY'

def get_chatgpt_response(query):
    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a stress and anxiety relief bot."},
                {"role": "user", "content": query}
            ],
            max_tokens=5
        )
        # Adjust based on actual response format
        return response.choices[0].text
    except Exception as e:
        # Print API errors to the console
        print(f"Error getting ChatGPT response: {e}")
        return "Error getting response from ChatGPT"