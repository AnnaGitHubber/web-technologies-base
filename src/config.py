from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

templates = Jinja2Templates(directory="src/templates")
static_files = StaticFiles(directory="src/static")
