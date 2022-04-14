from locale import T_FMT_AMPM
from termios import TAB0
from fastapi import FastAPI, HTTPException
from models import ToDo, toDoIn, toDoPydantic
from pydantic import BaseModel
from tortoise.contrib.fastapi import register_tortoise, HTTPNotFoundError
from uvicorn import run
from typing import List


class Message(BaseModel):
    message: str


app = FastAPI()

@app.get('/')
async def root():
    return {"path": "root"}



@app.get("/todos/", response_model=List[toDoPydantic], responses={404: {"model": HTTPNotFoundError}})
async def all_todo():
    """retourne une liste des enregistrement avec la methode all"""

    # vu qu'on utilise un framework imbriquant la programmation asynchrone, le mot cléa await face a ce qu'il faut attendre a ce
    # que son execution se termine belle et bien avant de continuer
    return await toDoPydantic.from_queryset(ToDo.all())
    


@app.get("/todo/{id}/", response_model=toDoPydantic, responses={404: {"model": HTTPNotFoundError}})
async def get_one(id: int):
    return await toDoPydantic.from_queryset_single(ToDo.get(id= id))



# Le parametre responses prend comme valeur un dictionnaire,  c'est la reponse envoyée face une/des erreur(s) de fetch dans 
# la base des données.
# On specifie une reponse en json par status comme ici c'est si l'erreur a comme status 404
@app.post("/todo/", response_model=toDoPydantic, responses={404: {"model": HTTPNotFoundError}})
async def create(todo: toDoIn):

    # faire un enregistrement
    enrg = await ToDo.create(**todo.dict(exclude_unset=True))
    return await toDoPydantic.from_tortoise_orm(enrg)



@app.put("/todo/{id}/", response_model=toDoPydantic, responses={404: {"model": HTTPNotFoundError}})
async def update(id: int, todo: toDoIn):
    await ToDo.filter(id= id).update(**todo.dict(exclude_unset=True))
    return await toDoPydantic.from_queryset_single(ToDo.get(id= id))



@app.delete("/todo/{id}/", response_model=Message, responses={404: {"model": HTTPNotFoundError}})
async def delete(id: int):
    enrg = await ToDo.filter(id= id).delete()
    if not enrg:
        raise HTTPException(status_code=404, detail="todo not found")
    
    return Message(message="deletion successfully")



# configuration a la base des donnees
register_tortoise(
    app,
    db_url="sqlite://store.db",
    modules={"models": ['models']},
    generate_schemas=True,
    add_exception_handlers=True 
)

if __name__ == "__main__":
    run(app, host="localhost", port=8000)