from flask import Flask, render_template
from basura import db
from api import api_blueprint

app = Flask(__name__)

# Configuración de la base de datos PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:tu_contraseña@localhost/contenedor_basura'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa la base de datos
db.init_app(app)

# Registro del blueprint API
app.register_blueprint(api_blueprint, url_prefix="/api")

# Rutas para las vistas HTML
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/autor")
def autor():
    return render_template("autor.html")

@app.route("/mapa")
def mapa():
    return render_template("mapa.html")

if __name__ == "__main__":
    app.run(debug=True)
