from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/AI_models", response_class=HTMLResponse)
def ai_models(request: Request):
    return templates.TemplateResponse("AI_models.html", {"request": request})

@app.get("/about_us", response_class=HTMLResponse)
def about_us(request: Request):
    return templates.TemplateResponse("about_us.html", {"request": request})

@app.get("/contact_us", response_class=HTMLResponse)
def contact_us(request: Request):
    return templates.TemplateResponse("contact_us.html", {"request": request})

@app.get("/my_work", response_class=HTMLResponse)
def my_work(request: Request):
    return templates.TemplateResponse("my_work.html", {"request": request})

@app.get("/lungs_cancer_detection_model", response_class=HTMLResponse)
def my_work(request: Request):
    return templates.TemplateResponse("lungs_cancer_detection_model.html", {"request": request})


@app.get("/music_gen", response_class=HTMLResponse)
def my_work(request: Request):
    return templates.TemplateResponse("music_gen.html", {"request": request})


@app.get("/vector_art", response_class=HTMLResponse)
def my_work(request: Request):
    return templates.TemplateResponse("vector_art.html", {"request": request})