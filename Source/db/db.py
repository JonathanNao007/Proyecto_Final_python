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
    
    def createTableClientes(self):
        with self.getConnection() as conn:
            conn.execute("""
                            Create Table Clientes (
                                clave int AUTO_INCREMENT PRIMARY KEY,
                                nombre varchar(200) Not Null,
                                direccion varchar(300),
                                correo_electronico varchar(100),
                                telefono varchar(15));
                            """)
            
    def createTableMenu(self):
        with self.getConnection() as conn:
            conn.execute("""
                        Create Table Menu (
                            clave int AUTO_INCREMENT PRIMARY KEY,
                            nombre varchar(200) Not Null,
                            precio decimal(10,2) Not Null);
                        """)
        
    def createTablePedido(self):
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