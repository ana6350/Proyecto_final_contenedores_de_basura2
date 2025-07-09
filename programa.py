from flask import Flask, render_template, request, redirect, url_for
from basura import db, Basura
from api import api_blueprint
from shapely.geometry import Point
from geoalchemy2.shape import from_shape
from werkzeug.utils import secure_filename
import os
from datetime import datetime

app = Flask(__name__)

# Configuración de la base de datos PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:anacorrales@localhost:5432/contenedor_basura'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Carpeta para subir imágenes
UPLOAD_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Asegura que la carpeta exista
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Inicializa la base de datos
db.init_app(app)

# Registro del blueprint de la API
app.register_blueprint(api_blueprint, url_prefix="/api")

# Función para validar extensión
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Página de inicio
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/autor")
def autor():
    return render_template("autor.html")

@app.route("/mapa", methods=["GET", "POST"])
def mapa():
    if request.method == "POST":
        try:
            fecha_str = request.form.get("fecha")
            ubicacion = request.form.get("ubicacion")
            estado = request.form.get("estado")
            observacion = request.form.get("observacion")
            foto = request.files.get("foto")

            # Parsear la fecha del formulario
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()

            # Guardar imagen si es válida
            filename = None
            if foto and allowed_file(foto.filename):
                filename = secure_filename(foto.filename)
                foto.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # Punto por defecto (puedes mejorarlo luego con coordenadas del mapa)
            punto = from_shape(Point(-74.115069, 4.7423251), srid=4326)

            nueva = Basura(
                localizacion=punto,
                fecha=fecha,
                ubicacion=ubicacion,
                estado=estado,
                observacion=observacion,
                foto=filename if filename else "sin_foto.jpg"
            )

            db.session.add(nueva)
            db.session.commit()

            return redirect(url_for("mapa"))
        
        except Exception as e:
            return f"Error al procesar el formulario: {str(e)}"

    return render_template("mapa.html")

if __name__ == "__main__":
    app.run(debug=True)
