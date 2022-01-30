from app import db

#For table clientes
class Cliente(db.Model):
    __tablename__ = 'cliente'
    cliente_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cliente_nombre = db.Column(db.String(100), nullable=False)
    cliente_renta = db.relationship('Renta', backref='clienteRenta', lazy=True)

#For table contratos
class Renta(db.Model):
    __tablename__ = 'renta'
    renta_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    renta_cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.cliente_id'), nullable=False)
    renta = db.Column(db.String(100), nullable=False)
    renta_fecha = db.Column(db.Date, nullable=False)
    vigencia_fecha = db.Column(db.Date, nullable=False)
    devolucion_fecha = db.Column(db.Date, nullable=False)
    multa = db.Column(db.Numeric(10,2))

db.create_all()