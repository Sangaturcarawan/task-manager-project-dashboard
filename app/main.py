from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

# BASE_DIR = "/home/Sangnegarawan/task-manager-project-dashboard"
app = FastAPI()

tasks = [
    "Buy groceries",
    "Finish project",
    "Call the office"
    ]

# app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "app/static")), name="static")
# templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "app/templates"))

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):

    context = {
        "request": request,
        "username":"Faris",
        "tasks": tasks
    }
    return templates.TemplateResponse("index.html", context)

@app.post("/add-task")
async def add_task(task_name: str = Form(...)):
    tasks.append(task_name)
    return RedirectResponse(url="/", status_code=303)

@app.post("/delete-task")
async def delete_task(task_name: str = Form(...)):
    if task_name in tasks:
        tasks.remove(task_name)
    return RedirectResponse(url="/", status_code=303)

@app.get("/dashboard", response_class=HTMLResponse)
async def read_dashboard(request: Request):

    context = {
        "request": request
    }
    return templates.TemplateResponse("dashboard.html", context)

@app.get("/login", response_class=HTMLResponse)
async def read_login(request: Request):

    context = {
        "request": request
    }
    return templates.TemplateResponse("login.html", context)


