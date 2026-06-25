import sqlite3
import os

class BaseDatos:
    def __init__(self, nombreDb):
        self.nombreDb = nombreDb

    def crearBaseDatos(self):
        if not os.path.exists(self.nombreDb):
            conn = sqlite3.connect(self.nombreDb)
            conn.close();

    def getConnection(self):
        conn = sqlite3.connect(self.nombreDb)
        conn.execute("PRAGMA foreign_keys = ON")
        return conn
    
    def table_exist(self, table_name):
        with self.getConnection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' And name = ?", (table_name,))
            exists = cursor.fetchone() is not None    
            return exists

    def createTableClientes(self):
        if not self.table_exist("Clientes"):
            with self.getConnection() as conn:            
                conn.execute("""
                                Create Table If Not Exist Clientes (
                                    clave int AUTO_INCREMENT PRIMARY KEY,
                                    nombre varchar(200) Not Null,
                                    direccion varchar(300),
                                    correo_electronico varchar(100),
                                    telefono varchar(15));
                                """)
            
    def createTableMenu(self):
        if not self.table_exist("Menu"):
            with self.getConnection() as conn:
                conn.execute("""
                            Create Table Menu (
                                clave int AUTO_INCREMENT PRIMARY KEY,
                                nombre varchar(200) Not Null,
                                precio decimal(10,2) Not Null);
                            """)
        
    def createTablePedido(self):
        if not self.table_exist("Pedido"):
            with self.getConnection() as conn:
                conn.execute("""
                            Create Table Pedido (
                                id int AUTO_INCREMENT PRIMARY KEY, 
                                pedido int Not Null,
                                cliente int Not Null,
                                producto int Not Null, 
                                precio decimal(10,2) Not Null,
                                fecha datetime,
                                cancelado bit Not Null Default(0),
                                FOREIGN KEY (cliente) REFERENCES Clientes(clave),
                                FOREIGN KEY (producto) REFERENCES Menu(clave));
                            """)