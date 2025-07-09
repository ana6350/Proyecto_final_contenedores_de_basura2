from flask import Flask, render_template, request, redirect, url_for
from basura import db, Contenedor
from api import api_blueprint
from shapely.geometry import Point
from geoalchemy2.shape import from_shape
from werkzeug.utils import secure_filename
import os
from datetime import datetime

app = Flask(__name__)

# Configuración de la base de datos PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:anacorrales@localhost:5432/basura_contenedor'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Carpeta para subir imágenes
UPLOAD_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Inicializar base de datos y registrar API
db.init_app(app)
app.register_blueprint(api_blueprint, url_prefix="/api")

# Validación de archivos permitidos
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Rutas principales
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
            direccion = request.form.get("direccion")
            estado = request.form.get("estado")
            observacion = request.form.get("observacion")
            foto = request.files.get("foto")
            lat = float(request.form.get("lat"))
            lon = float(request.form.get("lon"))

            # Parsear fecha
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()

            # Procesar imagen
            filename = None
            if foto and allowed_file(foto.filename):
                filename = secure_filename(foto.filename)
                foto.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # Crear punto geográfico
            punto = from_shape(Point(lon, lat), srid=4326)

            # Crear registro
            nuevo = Contenedor(
                localizacion=punto,
                fecha=fecha,
                direccion=direccion,
                estado=estado,
                observacion=observacion,
                foto=filename if filename else "sin_foto.jpg"
            )

            db.session.add(nuevo)
            db.session.commit()

            # ✅ Redirecciona con mensaje de éxito
            return redirect(url_for("mapa", exito=1))

        except Exception as e:
            return f"Error al procesar el formulario: {str(e)}"

    return render_template("mapa.html")
    
if __name__ == "__main__":
    app.run(debug=True)
