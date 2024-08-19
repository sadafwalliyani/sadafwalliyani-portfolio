from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Create a new FastAPI instance
app = FastAPI()

# Set up Jinja2 templates
templates = Jinja2Templates(directory=r"D:\\sadafwalliyani-portfolio\\templates")


# Route for the Home page
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

# Route for the About Us page
@app.get("/about", response_class=HTMLResponse)
def about(request: Request):
    return templates.TemplateResponse("about_us.html", {"request": request})

# Route for the Contact Us page
@app.get("/contact", response_class=HTMLResponse)
def contact(request: Request):
    return templates.TemplateResponse("contact_us.html", {"request": request})

# Route for generating text or any other functionality you want to add later
@app.get("/generate", response_class=HTMLResponse)
def generate(request: Request, text: str):
    # Here, you could add any processing logic if needed
    output = f"You entered: {text}"  # Example output

    # Pass the output to the result template
    return templates.TemplateResponse("home.html", {"request": request, "output": output})
