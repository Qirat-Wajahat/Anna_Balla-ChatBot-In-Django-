import openai  # OpenAI package
from openai.error import OpenAIError  # Generic OpenAI error handling
from .say import say

# Asynchronous function to interact with OpenAI chatbot
async def chatbot(query):
    openai.api_key = "sk-OlVdxa9EPE6q9zUzxQ7PE9QavNPCm8eEA9TIurQXsET3BlbkFJhhgjuaGefg4a9ATUcUevN3S5A3ffU87AdQ9BN2QHgA"  # Set the OpenAI API key

    try:
        # Call the OpenAI API using the new method
        completion = await openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": query}
            ]
        )

        chatbot_response = completion['choices'][0]['message']['content']  # Get the chatbot response
        print("\n Anna Balla:", chatbot_response)
        say(chatbot_response)  # Speak the chatbot response

    except OpenAIError as e:
        print(f"\n An error occurred. Details: {e}")
        return f"\n An error occurred. Details: {e}"
    return chatbot_response

  # chatbot_response = asyncio.run(chatbot(query))
        # print(f"Anna Balla: {chatbot_response}")
        # say(chatbot_response)
        # return chatbot_response