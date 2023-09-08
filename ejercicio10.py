# Este programa pregunta por consola por los productos de una cesta de la compra, separados por comas, y muestra por pantalla cada uno de los productos en una línea distinta.
# Primero, pedimos al usuario que introduzca los productos de su cesta de la compra, separados por comas.
productos = input("Introduce los productos de tu cesta de la compra, separados por comas: ")
# A continuación, convertimos la cadena de texto introducida por el usuario en una lista de productos.
productos = productos.split(",")
# Por último, mostramos por pantalla cada uno de los productos de la lista, en una línea distinta.
for producto in productos:
    print(producto)
