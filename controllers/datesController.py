from flask import Flask, render_template, request
from app import app
from models.models import *

@app.route('/', methods=['GET', 'POST'])
def index():
    contracts = Renta.query.all()
    filteredContracts = []
    if request.method == 'POST':
        initialDate = request.form['initialDate']
        endDate = request.form['endDate']
        filteredContracts = Renta.query.filter(Renta.renta_fecha >= initialDate, Renta.devolucion_fecha <= endDate).all()
        dic = {filcon.clienteRenta.cliente_nombre : 0 for filcon in filteredContracts}
        for con in filteredContracts:
            nombre_cliente = con.clienteRenta.cliente_nombre
            multa = con.multa + dic.get(nombre_cliente)
            dic.update({nombre_cliente : multa})
        filteredContracts = dic.items()
    return render_template('index.html', contracts = contracts, filteredContracts = filteredContracts)
