# tortoise est l'ORM python à utiliser


from fastapi import FastAPI, HTTPException
from models import Account, accountIn, accountOut
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise
from pydantic import BaseModel
from uvicorn import run


class Message(BaseModel):
    message: str
    
app= FastAPI()

@app.get("/")
async def home():
    return {"path": "root"}

@app.get("/account/{id}", response_model= accountOut, responses= {404: {"model": HTTPNotFoundError}})
async def read(id: int):
    enrgs= Account.get(id= id)
    return await accountOut.from_queryset_single(enrgs)

@app.post("/account", response_model=accountOut, responses={404: {"model": HTTPNotFoundError}})
async def create(account: accountIn):
    
    enrg= await Account.create(**account.dict(exclude_unset= True))
    return await accountOut.from_tortoise_orm(enrg)

@app.put("/account/{id}", response_model= accountOut, responses= {404: {"model": HTTPNotFoundError}})
async def update(id: int, newAccount: accountIn):
    
    await Account.filter(id= id).update(**newAccount.dict(exclude_unset= True))
    return await accountOut.from_queryset_single(Account.get(id= id))

@app.delete("/account/{id}", response_model= Message, responses={404: {"model": HTTPNotFoundError}})
async def delete(id: int):
    account= await Account.filter(id= id).delete()
    if not account:
        # si on n'a pas pu pointé le compte
        raise HTTPException(status_code=404, detail="compte non trouvée")
    
    
    return Message(message= "supprimée")
        
    
register_tortoise(app,
                db_url="mysql://root:@localhost/api_rest",
                modules={'models': ['models']},
                generate_schemas=True,
                add_exception_handlers=True)


    
if __name__ == "__main__":
    run(app, host="localhost", port=3000)
