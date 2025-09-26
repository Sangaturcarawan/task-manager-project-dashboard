from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
import os

# BASE_DIR = "/home/Sangnegarawan/task-manager-project-dashboard"
app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="halkita!9801")
tasks = [
    "Buy groceries",
    "Finish project",
    "Call the office"
    ]

USERS = {
    "Faris": "password1",
    "Zachary": "password2",
    "Amirul": "password3"
}

# app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "app/static")), name="static")
# templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "app/templates"))

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


# HOME PAGE

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):

    if not request.session.get("user"):
        return RedirectResponse(url="/login")

    ctxt = {
        "request": request,
        "username": request.session["user"],
        "tasks": tasks
    }
    return templates.TemplateResponse("index.html", ctxt)

# LOGIN GET

@app.get("/login", response_class=HTMLResponse)
async def read_login(request: Request):

    ctxt = {
        "request": request
    }
    return templates.TemplateResponse("login.html", ctxt)

# LOGIN POST

@app.post("/login")
async def login(request: Request, 
                username: str = Form(...),
                password: str = Form(...)):
    
    er_ctxt = {"request": request,
               "error": "Invalid username or password"}
    
    if username in USERS and USERS[username] == password:
        request.session["user"] = username
        return RedirectResponse(url="/", status_code=303)
    else:
        return templates.TemplateResponse("login.html", er_ctxt)
    
# LOGOUT GET

@app.get("/logout")
async def logout(request: Request):
    request.session.pop("user", None)
    return RedirectResponse(url="/login")

# CRUD TASKS

@app.post("/add-task")
async def add_task(task_name: str = Form(...)):
    tasks.append(task_name)
    return RedirectResponse(url="/", status_code=303)

@app.post("/delete-task")
async def delete_task(task_name: str = Form(...)):
    if task_name in tasks:
        tasks.remove(task_name)
    return RedirectResponse(url="/", status_code=303)

# DASHBOARD PAGE

@app.get("/dashboard", response_class=HTMLResponse)
async def read_dashboard(request: Request):

    context = {
        "request": request
    }
    return templates.TemplateResponse("dashboard.html", context)




