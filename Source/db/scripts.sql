Create Table Clientes (
    clave int AUTO_INCREMENT PRIMARY KEY,
    nombre varchar(200) Not Null,
    direccion varchar(300),
    correo_electronico varchar(100),
    telefono varchar(15)
);

Create Table Menu (
    clave int AUTO_INCREMENT PRIMARY KEY,
    nombre varchar(200) Not Null,
    precio decimal(10,2) Not Null
);

Create Table Pedido (
    pedido int AUTO_INCREMENT PRIMARY KEY, 
    cliente int Not Null,
    producto int Not Null, 
    precio decimal(10,2) Not Null,
    fecha datetime,
    FOREIGN KEY (cliente) REFERENCES Clientes(clave),
    FOREIGN KEY (producto) REFERENCES Menu(clave)
);