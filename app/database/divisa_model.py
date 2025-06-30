from app.database import db
import uuid

class PrecioDivisa(db.Model):
    __tablename__ = "precio_divisa"
    id = db.Column(db.String(36), primary_key=True, default=lambda:str(uuid.uuid4()))
    divisa = db.Column(db.String(16), nullable=False)
    precio = db.Column(db.float)
    fecha_consulta = db.Column(db.Date)

    def __repr__(self) -> str:
        return f"Divisa {divisa}: {precio}"