from flask import Blueprint, render_template, request, redirect, url_for, send_file
from models.pedido import Pedido
from models.cliente import Cliente
from models.menu import Menu
import io
from datetime import datetime

pedido_bp = Blueprint("pedidos", __name__)
pedidos_model = Pedido()
menu_model = Menu()
cliente_model = Cliente()

@pedido_bp.route("/")
def index():
    return redirect(url_for("pedidos.listar_pedidos"))

@pedido_bp.route("/pedidos")
def listar_pedidos():
    pedidos = pedidos_model.obtener()
    return render_template("pedidos.html", pedidos=pedidos)

@pedido_bp.route("/pedido/<int:pedido_id>")
def agrega_pedido(pedido_id):
    api = "pedidos.crea_pedido"
    accion = "Crear"
    pedido_id_db = pedidos_model.obtener_pedido_id()
    print(pedido_id_db)
    pedido = pedido_id_db[0]
    clavePedido = pedido_id if pedido_id is not None and pedido_id >= 0 else 0
    clientes = cliente_model.obtener_info_select()
    productos = menu_model.obtener_info_select()
    return render_template("pedido_add.html", pedido=pedido, API=api, accion = accion, clavePedido = clavePedido, dataClientes=clientes, dataProductos=productos)

@pedido_bp.route("/pedido/nuevo", methods=["POST"])
def crea_pedido():
    pedido = request.form.get("pedido")
    cliente = request.form.get("cliente_select")
    producto = request.form.get("producto_select")
    precio = request.form.get("precio")
    fecha = request.form.get("fecha_pedido")
    cancelado = 0
    pedidos_model.crear(pedido=pedido, cliente=cliente, producto=producto, precio=precio, fecha=fecha, cancelado=cancelado)
    return redirect(url_for("pedidos.listar_pedidos"))

@pedido_bp.route("/pedido/<int:pedido_id>/cancela", methods=["POST"])
def cancela_pedido(pedido_id):
    pedidos_model.cancelar(pedido=pedido_id)
    return redirect(url_for("pedidos.listar_pedidos"))

@pedido_bp.route("/pedido/<int:pedido_id>/imprime", methods=["POST"])
def imprimir_pedido(pedido_id):
    pedido = pedidos_model.obtener_id(pedido_id)[0]
    file_name = "mi_ticket_" + datetime.now().strftime("%Y%m%d%H%M%S") + "_.txt"
    mi_ticket = f"""        Mi ticket Folio:{pedido[1]} Fecha: {pedido[7]}
        Cliente: {pedido[3]}
        Producto: {pedido[5]}
        Precio: {pedido[6]}
                    """
    byte_stream = io.BytesIO(mi_ticket.encode('utf-8'))
    return send_file(
        byte_stream,
        mimetype='text/plain',
        as_attachment=True,
        download_name=file_name
    )
