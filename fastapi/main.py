from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

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