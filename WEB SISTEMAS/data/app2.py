from flask import Flask, send_from_directory, send_file
import os

# Ruta base del proyecto en PythonAnywhere
BASE_PATH = r"D:\WEB SISTEMAS\data"
app = Flask(__name__, static_folder=os.path.join(BASE_PATH, "static"))

@app.route("/")
def index():
    index_file = os.path.join(BASE_PATH, "index.html")
    if os.path.isfile(index_file):
        return send_file(index_file)
    return "<h1>No se encontró index.html en la carpeta /data</h1>"

@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory(os.path.join(BASE_PATH, "static"), filename)

if __name__ == "__main__":
    app.run(debug=True)
