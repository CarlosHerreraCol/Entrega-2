from paquete1 import Cliente


cliente1 = Cliente(nombre="Carlos Pineda", id_cliente="00345", correo="carlos.pineda@example.com", saldo=600)


cliente1.agregar_producto("Teléfono", 300)
cliente1.agregar_producto("Funda protectora", 350)


cliente1.comprar()


print(cliente1)