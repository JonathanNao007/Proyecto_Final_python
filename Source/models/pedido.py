from db.db import BaseDatos

class Pedido:
    def __init__(self, db_name = 'db_proyect.sqlite'):
        self.db = BaseDatos(db_name)

    # Crud basico
    def obtener_pedido_id(self):
        with self.db.getConnection() as conn:
            return conn.execute("""Select COALESCE(Max(pedido),0) + 1 As pedido From Pedido order By pedido desc Limit 1""").fetchone()

    def obtener(self):
        with self.db.getConnection() as conn:
            return conn.execute("""Select 
                                    p.pedido,
                                    c.nombre As cliente,
                                    p.precio,
                                    p.fecha,
                                    p.cancelado
                                    From Pedido p 
                                    join Clientes c on p.cliente = c.clave
                                    GROUP By p.pedido, c.nombre, p.precio, p.fecha""").fetchall()
        
    def obtener_id(self, clavePedido):
        with self.db.getConnection() as conn:
            return conn.execute("""Select 
                                    p.id,
                                    p.pedido,
                                    c.clave As claveCliente,
                                    c.nombre As cliente,
                                    m.clave As claveProducto,
                                    m.nombre As producto,
                                    p.precio,
                                    p.fecha,
                                    p.cancelado
                                    From Pedido p 
                                    Join Menu m On p.producto = m.clave
                                    join Clientes c on p.cliente = c.clave
                                    Where p.pedido = ?""", (clavePedido,)).fetchall()
    
    def crear(self, pedido, cliente, producto, precio, fecha, cancelado):
        with self.db.getConnection() as conn:
            cursor = conn.execute(
                "Insert Into Pedido(pedido, cliente, producto, precio, fecha, cancelado) Values(?,?,?,?,?,?)", (pedido, cliente, producto, precio, fecha, cancelado)
            )
            conn.commit()
            return cursor.lastrowid
        
    def cancelar(self, pedido):
        with self.db.getConnection() as conn:
            conn.execute(
                "Update Pedido Set cancelado = 1 Where pedido = ?;", (pedido,)
            )
            conn.commit()