from flask import Flask, render_template, request, redirect, url_for
from basura import db
from api import api_blueprint

app = Flask(__name__)

# Configuración de la base de datos PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:tu_contraseña@localhost/bk_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa la base de datos
db.init_app(app)

# Registro del blueprint de la API
app.register_blueprint(api_blueprint, url_prefix="/api")

# Página de inicio - descripción del proyecto
@app.route("/")
def index():
    return render_template("index.html")

# Página del referente teórico
@app.route("/about")
def about():
    return render_template("about.html")

# Página del autor
@app.route("/autor")
def autor():
    return render_template("autor.html")

# Página del mapa y formulario
@app.route("/mapa", methods=["GET", "POST"])
def mapa():
    if request.method == "POST":
        id_ = request.form.get("id")
        descripcion = request.form.get("descripcion")
        estado = request.form.get("estado")

        # Aquí podrías guardar en la base de datos si tienes un modelo definido
        print("Formulario recibido:")
        print(f"ID: {id_}")
        print(f"Descripción: {descripcion}")
        print(f"Estado: {estado}")

        return redirect(url_for("mapa"))

    return render_template("mapa.html")

if __name__ == "__main__":
    app.run(debug=True)