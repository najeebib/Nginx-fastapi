from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse

templates = Jinja2Templates(directory="templates")

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello from fast api"}

@app.get("/welcome-img")
def image():
    file_path = "images/welcome.jpg"
    return FileResponse(file_path)

@app.get("/welcome-html")
def html(request: Request):
    return templates.TemplateResponse("welcome.html", {"request": request})