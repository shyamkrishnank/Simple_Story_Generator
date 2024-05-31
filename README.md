# Fun Story writing Api - FastApi, Supabase, Generative AI

This project is a simple and fun application that leverages FastAPI, Supabase, and Generative AI to create engaging stories with user-defined characters.

## Installation

1. Create Environment

   python -m venv venv<br>
   source venv/bin/activate  # On Windows use `venv\Scripts\activate

1. Clone the repository:

   git clone https://github.com/shyamkrishnank/Simple_Story_Generator.git<br>
   cd Simple_Story_Generator

2. Install dependencies:

   pip install -r requirements.txt

3. Run the FastAPI application:

   uvicorn main:app --reload

# API Endpoints

  # Create Character
      
       URL : '/api/create_character'
       Method : POST

       Curl :
           curl -X 'POST' \
             'http://127.0.0.1:8000/api/create_character' \
             -H 'accept: application/json' \
             -H 'Content-Type: application/json' \
             -d '{
             "name": "Arun",
             "details": "A Brave Student"
           }'

       Response body :
           {
            "message": "Character added succesfully",
            "data": [
                {
                "id": 14,
                "created_at": "2024-05-30T12:34:47.238893+00:00",
                "name": "Arun",
                "details": "A Brave Student"
                }
            ]
            }

  # Generate Story (can send character id or character name)
      
       URL : '/api/generate_story'
       Method : POST
       
       Curl :
           curl -X 'POST' \
            'http://127.0.0.1:8000/api/generate_story' \
            -H 'accept: application/json' \
            -H 'Content-Type: application/json' \
            -d '{
            "character": "Arun"
            }'

       Response body :
           {
            "message": "Story created succesfully",
            "data": "Arun, a valiant student, stood unwavering in the face of adversity. His quick thinking and unwavering determination helped him conquer a menacing storm, ensuring the safety of his fellow students. The tempestuous winds had whipped up treacherous waves, but Arun's spirit remained unbroken. With his comrades huddled together in terror, he devised a plan to navigate the treacherous waters, guiding them through the storm and back to shore."
            }


 
 