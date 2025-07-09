from flask import Blueprint, request, jsonify
from modelo import Contenedor
from db import db
from datetime import date
from geoalchemy2.shape import from_shape
from shapely.geometry import Point

api_blueprint = Blueprint("api", __name__)

@api_blueprint.route("/nuevo", methods=["POST"])
def crear_contenedor():
    data = request.get_json()

    try:
        lat = float(data["lat"])
        lon = float(data["lon"])
        direccion = data["direccion"]
        estado = data["estado"]
        observacion = data["observacion"]

        punto = from_shape(Point(lon, lat), srid=4326)

        nuevo = Contenedor(
            localizacion=punto,
            fecha=date.today(),
            direccion=direccion,
            estado=estado,
            observacion=observacion,
            foto="sin_foto.jpg"
        )
        db.session.add(nuevo)
        db.session.commit()

        return jsonify({"mensaje": "Registro creado exitosamente"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@api_blueprint.route("/todos", methods=["GET"])
def obtener_todos():
    registros = Contenedor.query.all()
    resultado = []
    for r in registros:
        resultado.append({
            "id": r.id,
            "fecha": r.fecha.isoformat(),
            "direccion": r.direccion,
            "estado": r.estado,
            "observacion": r.observacion,
            "foto": r.foto,
            "localizacion": r.localizacion.desc # WKT (Well-Known Text)
        })
    return jsonify(resultado)
