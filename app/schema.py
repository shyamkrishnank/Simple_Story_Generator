from pydantic import BaseModel


class CharacterRequest(BaseModel):
    name : str
    details : str


class GenerateStoryRequest(BaseModel):
    character : int | str