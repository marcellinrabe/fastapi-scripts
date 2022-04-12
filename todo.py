
# api todo list
# la base de données est une liste
# si un todo n'existe pas lever une exception http 404 en utilisant fastapi
# realiser un crud: create read update delete
# verbes get post update delete

from http.client import HTTP_PORT
from turtle import st
from fastapi import FastAPI, HTTPException
from typing import Optional, List
from pydantic import BaseModel
import uvicorn

root = FastAPI(title="API todo list", version="v1")

# un todo
class ToDo(BaseModel):
    company: str
    project: str
    name: str
    dueDate : str
    description: Optional[str] = None  

# la base des données
todos = []

@root.get('/')
async def home():

    return({"title": "Les taches"})

@root.get('/todos/', response_model=List[ToDo])
async def get_todos():
    """
        Il est tout à fait possible de faire en sorte de renvoyer une liste
        avec fastapi, néan-moins la reponse est en réalité en json.
        C'est juste de faire en sorte XD
    """

    return todos

@root.get("/todo/{id}/")
async def get_todo(id: int):
    try:

        return todos[id]
    except:

        raise HTTPException(status_code=404, detail="tache non trouvé")

@root.post("/todos/add/")
async def add(new_ToDo: ToDo):

    todos.append(new_ToDo)
    return new_ToDo

@root.put("/todos/update/{id}/")
async def update(id: int, new_ToDo: ToDo):
    try:
        todos[id] = new_ToDo
        return todos[id]
    except:
        raise HTTPException(status_code=404, detail="tache non trouvé")

@root.delete("/todos/delete/{id}")
async def delete(id: int):

    try:
        todo_deleted = todos[id]
        todos.pop(id)
        return todo_deleted
    except:
        raise HTTPException(status_code=404, detail="tache non trouvé")



# lancement du fichier
if __name__ == "__main__":
    uvicorn.run(root, host="localhost", port=3000)

