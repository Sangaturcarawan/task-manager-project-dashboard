import sys
import os
from fastapi.middleware.wsgi import WSGIMiddleware

# +++++++++++ PROJECT PATH +++++++++++
project_path = '/home/Sangnegarawan/task-manager-project-dashboard'
if project_path not in sys.path:
    sys.path.append(project_path)

# +++++++++++ VIRTUALENV +++++++++++
# Make sure your Web tab points to this virtualenv:
# /home/Sangnegarawan/.virtualenvs/.venv/

# +++++++++++ IMPORT FASTAPI APP +++++++++++
from app.main import app as fastapi_app

# +++++++++++ WRAP FASTAPI IN WSGI MIDDLEWARE +++++++++++
application = WSGIMiddleware(fastapi_app)

# +++++++++++ OPTIONAL: FORCE WORKING DIRECTORY +++++++++++
# This ensures relative paths (like templates/static) work correctly
os.chdir(project_path)
