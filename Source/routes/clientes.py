from flask import Blueprint, render_template, request, redirect, url_for
from models.cliente import Cliente

cliente_bp = Blueprint("clientes", __name__)
clientes_model = Cliente()

@cliente_bp.route("/clientes")
def listar_clientes():
    clientes = clientes_model.obtener()
    return render_template("clientes.html", clientes=clientes)

@cliente_bp.route("/clientes/<int:cliente_id>")
def agrega_edita_clientes(cliente_id):
    api = "clientes.crea_cliente"
    accion = "Crear"
    cliente = {}
    claveCliente = cliente_id if cliente_id is not None and cliente_id >= 0 else 0
    if cliente_id > 0:
        api = "clientes.edita_cliente"
        accion = "Editar"
        cliente = clientes_model.obtener_id(cliente_id)
    return render_template("cliente_add_edit.html", cliente=cliente, API=api, accion = accion, claveCliente = claveCliente)

@cliente_bp.route("/cliente/nuevo", methods=["POST"])
def crea_cliente():
    nombre = request.form.get("nombre")
    direccion = request.form.get("direccion")
    correo_electronico = request.form.get("email")
    telefono = request.form.get("telefono")
    if nombre and direccion and correo_electronico and telefono:
        clientes_model.crear(nombre=nombre, direccion=direccion, correo_electronico=correo_electronico, telefono=telefono)
    return redirect(url_for("clientes.listar_clientes"))

@cliente_bp.route("/cliente/<int:cliente_id>/edita", methods=["POST"])
def edita_cliente(cliente_id):
    claveCliente = cliente_id
    nombre = request.form.get("nombre")
    direccion = request.form.get("direccion")
    correo_electronico = request.form.get("email")
    telefono = request.form.get("telefono")
    if nombre and direccion and correo_electronico and telefono:
        clientes_model.actualizar(nombre=nombre, direccion=direccion, correo_electronico=correo_electronico, telefono=telefono, claveCliente=claveCliente)
    return redirect(url_for("clientes.listar_clientes"))

@cliente_bp.route("/cliente/<int:cliente_id>/eliminar", methods=["POST"])
def elimina_cliente(cliente_id):
    clientes_model.eliminar(cliente_id)
    return redirect(url_for("clientes.listar_clientes"))