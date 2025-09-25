from fastapi.middleware.wsgi import WSGIMiddleware
from app.main import ass as fastapi_app

application =   WSGIMiddleware(fastapi_app)