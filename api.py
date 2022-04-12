from fastapi import FastAPI, Form
from typing import Optional
from pydantic import BaseModel
import uvicorn


# l'objet de reponse du requete post
class response(BaseModel):
    name: str
    firstName: str
    age: int
    color: Optional[str] = None


app = FastAPI()



@app.get("/")
async def hello():
    return {"hello": "world"}

@app.get('/sections/{numero}')
async def goTo(numero: int):
    return {"section": numero}


# requete de type post
@app.post('/me/{name}', response_model=response, response_model_exclude={'age'})
async def datas(response: response, name: str, color: Optional[str]):
    if name == "marcellin":
        response.name = "RABE"
        response.firstName = "Marcellin"
        response.age = 18

    if color.strip() == "maroon":
        response.color= "maroon"

    return response

@app.post('/login/')
async def login(username: str = Form(...), password: str = Form(...)):
    
    return username

# si le fichier est directement executé alors lancer le serveur
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
