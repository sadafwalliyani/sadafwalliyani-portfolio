from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Create a new FastAPI instance
app = FastAPI()

# Set up Jinja2 templates
templates = Jinja2Templates(directory=r'D:\sadafwalliyani-portfolio\templates')


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    print("Home page accessed")  # Add this line
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/AI_models", response_class=HTMLResponse)
def ai_models(request: Request):
    print("AI Models page accessed")  # Add this line
    return templates.TemplateResponse("AI_models.html", {"request": request})

@app.get("/about_us", response_class=HTMLResponse)
def about_us(request: Request):
    print("About Us page accessed")  # Add this line
    return templates.TemplateResponse("about_us.html", {"request": request})

@app.get("/contact_us", response_class=HTMLResponse)
def contact_us(request: Request):
    print("Contact Us page accessed")  # Add this line
    return templates.TemplateResponse("contact_us.html", {"request": request})

# Route for generating text or any other functionality you want to add later
@app.get("/generate", response_class=HTMLResponse)
def generate(request: Request, text: str):
    # Here, you could add any processing logic if needed
    output = f"You entered: {text}"  # Example output

    # Pass the output to the result template
    return templates.TemplateResponse("home.html", {"request": request, "output": output})
