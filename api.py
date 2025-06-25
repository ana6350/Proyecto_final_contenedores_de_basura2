from flask import Blueprint, request, jsonify
from basura import Basura
from db import db
from datetime import date
from geoalchemy2.shape import from_shape
from shapely.geometry import Point

api_blueprint = Blueprint("api", __name__)

@api_blueprint.route("/nueva", methods=["POST"])
def crear_basura():
    data = request.get_json()
    
    try:
        lat = float(data["lat"])
        lon = float(data["lon"])
        ubicacion = data["ubicacion"]
        estado = data["estado"]
        observacion = data["observacion"]

        punto = from_shape(Point(lon, lat), srid=4326)

        nueva = Basura(
            localizacion=punto,
            fecha=date.today(),
            ubicacion=ubicacion,
            estado=estado,
            observacion=observacion
        )
        db.session.add(nueva)
        db.session.commit()

        return jsonify({"mensaje": "Registro creado exitosamente"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@api_blueprint.route("/todos", methods=["GET"])
def obtener_todos():
    registros = Basura.query.all()
    resultado = []
    for r in registros:
        punto = r.localizacion.desc  # formato WKT
        resultado.append({
            "id": r.id,
            "fecha": r.fecha.isoformat(),
            "ubicacion": r.ubicacion,
            "estado": r.estado,
            "observacion": r.observacion,
            "localizacion": punto
        })
    return jsonify(resultado)
