from fastapi import FastAPI
from typing import List,Optional
from pydantic import BaseModel,Field
app=FastAPI()

class room(BaseModel):
    id:str=None
    category:str=None
class occupants(room):
    id:Optional[str]=None
    category:Optional[str]=None
    name:str=None
    age:int=None
    package:str=None

@app.post("/{room}")
async def update_rooms(room:str):
    pass
    