from app.database import db
import uuid

class Signos(db.Model):
    __tablename__ = "signos"
    id = db.Column(db.String(36), primary_key=True, default=lambda:str(uuid.uuid4()))
    nombre = db.Column(db.String(15))
    fecha_inicio = db.Column(db.Date)
    fecha_fin = db.Column(db.Date)
    caracteristicas = db.Column(db.String(400))

class Predicciones(db.Model):
    __tablename__ = "predicciones"
    id = db.Column(db.String(36), primary_key=True, default=lambda:str(uuid.uuid4()))
    fecha = db.Column (db.Date)
    signos = db.Column(db.String(15), db.ForeignKey("signos.nombre"))
    prediccion = db.Column (db.String(500))

class Imagenes(db.Model):
    __tablename__ = "imagenes"
    id = db.Column(db.String(36), primary_key=True, default=lambda:str(uuid.uuid4()))
    signos = db.Column(db.Date)
    ubicacion = db.Column(db.String(15), nullable=True)