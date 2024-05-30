import os
import google.generativeai as genai
from dotenv import load_dotenv

genai.configure(api_key=os.getenv("GENAI_KEY"))


generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 0,
  "max_output_tokens": 2048,
  "response_mime_type": "text/plain",
}
safety_settings = []

model = genai.GenerativeModel(
  model_name="gemini-1.0-pro",
  safety_settings=safety_settings,
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[]
)

def generate_story(input):
    try:
        name = input['name']
        detail = input['details']
        #prompt to create a story based on the name and details
        response = chat_session.send_message(f'Write a short story about the character named {name} who is {detail} in 4 or 5 sentence')
        return response.text
    except Exception as e:
        return {'text':"Sorry currently can't create story"}
