# Descripcion del proyecto
Proyecto realizado en python, sqlite y flask 
Con el objetivo de crear pedidos, tambien con la posibilidad de cancelarlos e imprimir un txt con el detalle.
Esto con el uso de tres tablas Clientes, Menu y Pedidos. Teniendo la posibilidad de crear, modificar y eliminar tanto clientes como productos de Menu.

# CONFIGURACIÓN 
# Entorno virtual /venv activación 
# Creacion python -m venv venv
venv\Scripts\activate

# Instalacion de dependencias, solo en caso de ser necesario(*pip freeze > requirements.txt)
pip install -r requirements.txt

# Ejecucion dentro del la carpeta Source
# Para desarrollo y tener hotreload
flask run --debug
# Para ejecucion normal
flask run 