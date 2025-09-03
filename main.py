from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app=FastAPI()

@app.get("/ping")
def pong():
 return{"message":"pong"}

@app.get("/health")
def health_root():
 return{"message":"ok"}


class phone(BaseModel):
 identifiant: str
 brand: str
 model: str
 characters:List[object]=[]

resultat:List[phone]=[]

@app.post("/phone")
 def phone(phone:phone):

