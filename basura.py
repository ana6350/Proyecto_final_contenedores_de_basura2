from db import db
from sqlalchemy import Column, Integer, String, Date
from geoalchemy2 import Geometry

class Basura(db.Model):
    __tablename__ = 'basura'

    id = Column(Integer, primary_key=True, autoincrement=True)
    localizacion = Column(Geometry(geometry_type='POINT', srid=4326), nullable=False)
    fecha = Column(Date, nullable=False)
    ubicacion = Column(String(100), nullable=False)
    estado = Column(String(100), nullable=False)
    observacion = Column(String(300), nullable=False)
    foto = Column(String(100), nullable=False)

    def __repr__(self):
        return f"<Basura id={self.id} ubicacion={self.ubicacion} estado={self.estado}>"
