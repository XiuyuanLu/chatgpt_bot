from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv('CHATGPT_API_KEY')


def chatgpt_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=2000
    )
    response_dict = response.get('choices')
    if response_dict and len(response_dict) > 0:
        prompt_response = response_dict[0]['text']
    return prompt_response
