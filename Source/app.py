from flask import Flask
from db.db import BaseDatos
from routes.pedidos import pedido_bp
from routes.clientes import cliente_bp
from routes.menu import menu_bp

app = Flask(__name__)

app.register_blueprint(pedido_bp)
app.register_blueprint(cliente_bp)
app.register_blueprint(menu_bp)

db = BaseDatos("db_proyect.sqlite")
db.crearBaseDatos()
db.createTableClientes()
db.createTableMenu()
db.createTablePedido()

if __name__ == "__main__":
    app.run(debug=True)

