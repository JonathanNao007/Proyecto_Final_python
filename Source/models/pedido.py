from db.db import BaseDatos

class Pedido:
    def __init__(self, db_name = 'db_proyect.sqlite'):
        self.db = BaseDatos(db_name)

    # Crud basico
    def obtener(self):
        with self.db.getConnection() as conn:
            return conn.execute("Select * From Pedido").fetchall()
        
    def obtener_id(self, clavePedido):
        with self.db.getConnection() as conn:
            return conn.execute("Select * From Pedido Where pedido = ?", (clavePedido)).fetchone()
    
    def crear(self, pedido, cliente, producto, precio, fecha, cancelado):
        with self.db.get_connection() as conn:
            cursor = conn.execute(
                "Insert Into Pedido(pedido, cliente, producto, precio, fecha, cancelado) Values(?,?,?,?,?,0)", (nombre, direccion, correo_electronico, telefono)
            )
            conn.commit()
            return cursor.lastrowid
        
    def cancelar(self, pedido):
        with self.db.get_connection() as conn:
            conn.execute(
                "Update Pedido Set cancelado = 1 Where pedido = ?;", (pedido)
            )
            conn.commit()