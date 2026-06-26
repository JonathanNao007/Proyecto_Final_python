from db.db import BaseDatos

class Cliente:
    def __init__(self, db_name = 'db_proyect.sqlite'):
        self.db = BaseDatos(db_name)

    # Crud basico
    def obtener(self):
        with self.db.getConnection() as conn:
            return conn.execute("Select * From Clientes").fetchall()
        
    def obtener_id(self, claveCliente):
        with self.db.getConnection() as conn:
            return conn.execute("Select * From Clientes Where clave = ?", (claveCliente,)).fetchone()
    
    def crear(self, nombre, direccion, correo_electronico, telefono):
        with self.db.getConnection() as conn:
            cursor = conn.execute(
                "Insert Into Clientes(nombre, direccion, correo_electronico, telefono) Values(?,?,?,?)", (nombre, direccion, correo_electronico, telefono)
            )
            conn.commit()
            return cursor.lastrowid
        
    def actualizar(self, nombre, direccion, correo_electronico, telefono, claveCliente):
        with self.db.getConnection() as conn:
            conn.execute(
                "Update Clientes Set nombre = ?, direccion = ?, correo_electronico = ?, telefono = ? Where clave = ?", (nombre, direccion, correo_electronico, telefono, claveCliente)
            )
            conn.commit()

    def eliminar(self, claveCliente):
        with self.db.getConnection() as conn:
            conn.execute(
                "Delete From Clientes Where clave = ?", (claveCliente,)
            )
            conn.commit()