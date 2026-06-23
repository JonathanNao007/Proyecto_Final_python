from flask import Flask
from db.db import BaseDatos

app = Flask(__name__)
app.secret_key = "S3cur3tyP4@55W0rd@"

db = BaseDatos("db_proyect.sqlite")
db.crearBaseDatos()
db.createTableClientes()
db.createTableMenu()
db.createTablePedido()

if __name__ == "__main__":
    app.run(debug=True)

