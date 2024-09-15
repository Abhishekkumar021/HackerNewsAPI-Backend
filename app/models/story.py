from pydantic import BaseModel
from datetime import datetime



class Story(BaseModel):
    title: str
    author:str
    url:str
    score:int
    time:str