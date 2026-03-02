from flask import Flask, send_from_directory, send_file
import os

# Definimos la ruta base de la carpeta del proyecto (WEB SISTEMAS)
# Salimos de 'data' para obtener la raíz del proyecto
BASE_DIR = r"D:\WEB SISTEMAS"
DATA_PATH = os.path.join(BASE_DIR, "data")
IMG_PATH = os.path.join(BASE_DIR, "img")

app = Flask(__name__)

@app.route("/")
def index():
    index_file = os.path.join(DATA_PATH, "index.html")
    if os.path.isfile(index_file):
        return send_file(index_file)
    return "<h1>No se encontró index.html en la carpeta /data</h1>"

# Nuevo endpoint para servir las imágenes desde la carpeta /img
@app.route("/img/<path:filename>")
def serve_images(filename):
    return send_from_directory(IMG_PATH, filename)

# Mantenemos static por si agregas CSS/JS externos luego
@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory(os.path.join(DATA_PATH, "static"), filename)

if __name__ == "__main__":
    app.run(debug=True)