from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from .schema import CharacterRequest, GenerateStoryRequest
from .supabase import supabase
from .util import generate_story

base_router = APIRouter(
    prefix='/api',
    tags=['Base Route'],
    responses={404: {"description": "Not found"}},
)


@base_router.post("/create_character") #route for creating the character
async def create_character_route(character: CharacterRequest):
     """
     Create a character with all the information:
     - **name**: each character must have a name
     - **details**: each character must have some details
     """
     try:
        if character.name and character.details:
            #query for saving the character in the supabase
            response = supabase.table('characters').insert({"name": character.name, "details": character.details}).execute()
            return JSONResponse(
                    status_code=201,
                    content={"message": "Character added succesfully","data":response.data},
                        ) 
        else:
            return JSONResponse(
                status_code=400,
                content={"message":"Please enter the valid name and details"}
            ) 
     except Exception as e:
        return JSONResponse(
                status_code=500,
                content={"message": "Oops! Something went wrong while adding character"},
            )     

@base_router.post("/generate_story")
async def generate_story_route(search : GenerateStoryRequest):
    """
    For generations story enter the character name or character id:
    """
    try:
        if search.character:
            if type(search.character) == int: #check whether the character is the id
                response = supabase.table('characters').select('*').eq('id', search.character).limit(1).execute()

                if not len(response.data): # if character not found on the id
                    return JSONResponse(
                           status_code=400,
                           content={'message':'Character with id not found'}
                        )           

            elif type(search.character) == str: #check whether the character is the name
                response = supabase.table('characters').select('*').eq('name', search.character).limit(1).execute() 

                if not len(response.data): # if character not found on the name
                    return JSONResponse(
                           status_code=400,
                           content={'message':'Character with name not found'}
                        )            
            else:
                return JSONResponse(
                        status_code=400,
                        content={"message": "Sorry! No characters found"},
                    )   
        
            story = generate_story(response.data[0]) # Generating story
            return JSONResponse(
                         status_code=201,
                         content={"message": "Story created succesfully","data":story},
                        )  
        else:
               return JSONResponse(
                        status_code=400,
                        content={"message":"Sorry! No characters found"},
                    )  
             
    except Exception as e:
              return JSONResponse(
                        status_code=400,
                        content={"message":"Enter the valid character"},
                    )  

        

