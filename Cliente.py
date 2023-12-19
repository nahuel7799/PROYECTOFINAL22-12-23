class Cliente:
    def __init__(self, nombre, email, direccion):
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.carrito = []

    def agregar_producto(self, producto):
        self.carrito.append(producto)

    def eliminar_producto(self, producto):
        if producto in self.carrito:
            self.carrito.remove(producto)
        else:
            print("El producto no está en el carrito")

    def realizar_compra(self):
        total = 0
        for producto in self.carrito:
            total += producto.precio
        print(f"Compra realizada por {self.nombre}. Total a pagar: {total}")