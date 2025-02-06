from data.database import database
from typing import Annotated
from data.dao.dao_juegos import DaoJuegos
from data.modelo.menu import Menu
from typing import Union
from fastapi import FastAPI, Request,Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def index(request: Request):
     return templates.TemplateResponse(
        request=request, name="Index.html"                    
    )

@app.get("/Fallout")
def Fallout(request: Request):
     return templates.TemplateResponse(
        request=request, name="HistoriaFallout.html"                  
    )


@app.get("/Doom")
def Doom(request: Request):
     return templates.TemplateResponse(
        request=request, name="PaginaDoom.html"                   
    )

@app.get("/Topjuegos")
def TopJuegos(request: Request):
     return templates.TemplateResponse(
        request=request, name="TopJuegos.html"                   
    )
     
@app.get("/juegos")
def get_juegos(request: Request,nombre : str = "usuario",otro: int  = 1):

    menu = Menu(True,True)
    juegos =  DaoJuegos().get_all(database)
   

    return templates.TemplateResponse(
    request=request, name="juegos.html", context={"menu": menu,"juegos": juegos,"nombre": nombre} )
   
   

@app.get("/deletejuegos/{juego_id}")
def delete_juegos(request: Request,juego_id:str):
    dao = DaoJuegos()
    dao.delete(database, juego_id)
    
    juegos =  dao.get_all(database)
    return templates.TemplateResponse(
    request=request, name="juegos.html", context={"juegos": juegos}                                                      
)

  

@app.post("/deljuegos")
def del_juegos(request: Request,juego_id:Annotated[str, Form()] ):
    print("hlhl")
    dao = DaoJuegos()
    dao.delete(database, juego_id)
    
    juegos =  dao.get_all(database)
    return templates.TemplateResponse(
    request=request, name="juegos.html", context={"juegos": juegos} )

@app.get("/formaddjuegos")
def form_add_juegos(request: Request):
    return templates.TemplateResponse(
    request=request, name="formaddJuegos.html"
    )

@app.post("/addjuegos")
def add_juegos(request: Request, nombre: Annotated[str, Form()] = None):
    if nombre is None:
        return templates.TemplateResponse(
        request=request, name="juegos.html", context={"nombre": "pepe"}
        )
    
    dao = DaoJuegos()
    dao.insert(database, nombre)
    
    juegos =  dao.get_all(database)
    return templates.TemplateResponse(
    request=request, name="formaddJuegos.html", context={"juegos": juegos}                                                      
)    