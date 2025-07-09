from flask import Flask, render_template, request, redirect, url_for
from basura import db, Basura
from api import api_blueprint
from datetime import date
from shapely.geometry import Point
from geoalchemy2.shape import from_shape
from werkzeug.utils import secure_filename
import os

# Configuración inicial
app = Flask(__name__)

# Configuración de base de datos PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:anacorrales@localhost:5432/contenedor_basura'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Carpeta para subir imágenes
UPLOAD_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Asegurar que la carpeta exista
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Inicializar base de datos
db.init_app(app)

# Registrar blueprint de la API
app.register_blueprint(api_blueprint, url_prefix="/api")

# Función para validar extensiones de archivo
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Página de inicio
@app.route("/")
def index():
    return render_template("index.html")

# Página sobre el proyecto
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
        foto = request.files.get("foto")

        filename = None
        if foto and allowed_file(foto.filename):
            filename = secure_filename(foto.filename)
            foto.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Puedes ajustar esta ubicación si capturas los clics del mapa
        punto = from_shape(Point(-74.115069, 4.7423251), srid=4326)

        nueva = Basura(
            id=int(id_),
            localizacion=punto,
            fecha=date.today(),
            ubicacion=descripcion,
            estado=estado,
            observacion="Desde formulario web",
            foto=filename if filename else "sin_foto.jpg"
        )

        db.session.add(nueva)
        db.session.commit()

        return redirect(url_for("mapa"))

    return render_template("mapa.html")

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run(debug=True)
