from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app= FastAPI()

template= Jinja2Templates(directory="views")

@app.get("/cv/", response_class=HTMLResponse)
async def read(request: Request, param: str):
    # preciser une variable de type requete est strictement indispensable pour renvoie 
    # le code html
    
    return template.TemplateResponse("index.html", {"request": request, "param": param})
    