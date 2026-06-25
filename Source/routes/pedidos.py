from flask import Blueprint, render_template, request, redirect, url_for
from models.pedido import Pedido

pedido_bp = Blueprint("pedidos", __name__)
pedidos_model = Pedido()

@pedido_bp.route("/")
def index():
    return redirect(url_for("pedidos.listar_pedidos"))

@pedido_bp.route("/pedidos")
def listar_pedidos():
    pedidos = pedidos_model.obtener()
    return render_template("pedidos.html", pedidos=pedidos)

