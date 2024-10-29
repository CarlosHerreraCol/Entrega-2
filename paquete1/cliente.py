
class Cliente:
    def __init__(self, nombre, id_cliente, correo, saldo):
        self.nombre = nombre
        self.id_cliente = id_cliente
        self.correo = correo
        self.saldo = saldo
        self.carrito = []

    def agregar_producto(self, producto, precio):
        self.carrito.append((producto, precio))
        print(f"{producto} ha sido agregado al carrito de {self.nombre} por ${precio}.")

    def comprar(self):
        total = sum(precio for _, precio in self.carrito)
        if total <= self.saldo:
            print(f"{self.nombre} ha comprado los siguientes productos: {', '.join(p for p, _ in self.carrito)} por un total de ${total}.")
            self.saldo -= total
            self.carrito = []  # Vacía el carrito después de la compra
        else:
            print(f"{self.nombre} no tiene suficiente saldo para completar la compra. Saldo actual: ${self.saldo}")

    def __str__(self):
        return f"Cliente: {self.nombre} (ID: {self.id_cliente}), Email: {self.correo}, Saldo: ${self.saldo}"