# Importamos lo necesario para crear la web y manejar archivos
from fastapi import FastAPI  
from fastapi.staticfiles import StaticFiles  
from fastapi.responses import FileResponse  
import os  

# Creamos la aplicación web
app = FastAPI()

# Hacemos accesible la carpeta "static" para que el navegador pueda ver sus archivos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Endpoint para el favicon (icono de la pestaña)
@app.get("/favicon.ico")
async def favicon():
    # Devuelve el archivo "favicon.png" que está dentro de "static"
    return FileResponse(os.path.join("static", "favicon.png"))