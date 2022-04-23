from socket import IP_DEFAULT_MULTICAST_LOOP
from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field
from typing import List
from db import *
from datetime import datetime


app= FastAPI()

class Register(BaseModel):
    id: int
    name: str
    created_at: datetime
    
class RegisterIn(BaseModel):
    name: str
    
    
# gerer requete via evenement par le lancement et
# la fermeture de la base des données
@app.on_event("startup")
async def connect():
    await database.connect()

@app.on_event("shutdown")
async def disconnect():
    await database.disconnect()

# crud
@app.post("/register", response_model=Register)
async def create(new : RegisterIn= Depends()):
    query= register.insert().values(
        name= new.name,
        created_at= datetime.utcnow)
    
    record_id= await database.execute(query)
    query= register.select().where(register.c.id== record_id)
    row= await database.fetch_one(query)
    return {**row}

@app.get("/register/{id}", response_model= Register)
async def read(id: int):
    query = register.select().where(register.c.id== id)
    user= database.fetch_one(query)
    return {**user}

@app.get("/register/", response_model= List[Register])
async def readAll():
    query= register.select()
    rows= database.fetch_all(query)
    return rows

@app.put("/register/{id}", response_model= Register)
async def update(id: int, new: RegisterIn= Depends()):
    query= register.update().where(register.c.id== id).values(
        username= new.name,
        created_at= datetime.utcnow 
    )
    
    record_id= database.execute(query)
    query= register.select().where(register.c.id== id)
    row= database.fetch_one(query)
    return {**row} 

@app.delete("/register/{id}")
async def delete(id: int):
    query= register.delete().where(register.c.id== id)
    return database.execute(query)

    