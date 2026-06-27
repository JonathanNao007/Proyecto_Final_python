from db.db import BaseDatos
from flask import jsonify

class Menu:
    def __init__(self, db_name = 'db_proyect.sqlite'):
        self.db = BaseDatos(db_name)

    # Crud basico
    def obtener(self):
        with self.db.getConnection() as conn:
            return conn.execute("Select * From Menu").fetchall()
        
    def obtener_json(self):
        with self.db.getConnection() as conn:
            data = conn.execute("Select clave, nombre, precio From Menu;").fetchall()
            headers = ['clave', 'nombre', 'precio']
            json_data = [dict(zip(headers, row)) for row in data]
            return (json_data)
        
    def obtener_info_select(self):
        with self.db.getConnection() as conn:
            return conn.execute("Select clave, nombre From Menu;").fetchall()
        
    def obtener_id(self, claveMenu):
        with self.db.getConnection() as conn:
            return conn.execute("Select * From Menu Where clave = ?", (claveMenu,)).fetchone()
    
    def crear(self, nombre, precio):
        with self.db.getConnection() as conn:
            cursor = conn.execute(
                "Insert Into Menu(nombre, precio) Values(?,?)", (nombre, precio)
            )
            conn.commit()
            return cursor.lastrowid
        
    def actualizar(self, nombre, precio, claveMenu):
        with self.db.getConnection() as conn:
            conn.execute(
                "Update Menu Set nombre = ?, precio = ? Where clave = ?", (nombre, precio, claveMenu)
            )
            conn.commit()

    def eliminar(self, claveMenu):
        with self.db.getConnection() as conn:
            conn.execute(
                "Delete From Menu Where clave = ?", (claveMenu,)
            )
            conn.commit()