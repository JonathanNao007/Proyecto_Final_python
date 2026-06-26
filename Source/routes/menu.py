from flask import Blueprint, render_template, request, redirect, url_for
from models.menu import Menu

menu_bp = Blueprint("menu", __name__)
menu_model = Menu()

@menu_bp.route("/menu")
def listar_menu():
    menu = menu_model.obtener()
    return render_template("menu.html", menu=menu)

@menu_bp.route("/menu/<int:menu_id>")
def agrega_edita_menu(menu_id):
    api = "menu.crea_menu"
    accion = "Crear"
    menu = {}
    claveMenu = menu_id if menu_id is not None and menu_id >= 0 else 0
    if claveMenu > 0:
        api = "menu.edita_menu"
        accion = "Editar"
        menu = menu_model.obtener_id(menu_id)
    return render_template("menu_add_edit.html", menu=menu, API=api, accion = accion, claveMenu = claveMenu)

@menu_bp.route("/menu/nuevo", methods=["POST"])
def crea_menu():
    nombre = request.form.get("nombre")
    precio = request.form.get("precio")
    if nombre and precio:
        menu_model.crear(nombre=nombre, precio=precio)
    return redirect(url_for("menu.listar_menu"))

@menu_bp.route("/menu/<int:menu_id>/edita", methods=["POST"])
def edita_menu(menu_id):
    claveMenu = menu_id
    nombre = request.form.get("nombre")
    precio = request.form.get("direccion")
    if nombre and precio:
        menu_model.actualizar(nombre=nombre, precio=precio, claveMenu=claveMenu)
    return redirect(url_for("menu.listar_menu"))

@menu_bp.route("/menu/<int:menu_id>/eliminar", methods=["POST"])
def elimina_menu(menu_id):
    menu_model.eliminar(menu_id)
    return redirect(url_for("menu.listar_menu"))