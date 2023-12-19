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

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

cliente1 = Cliente("Juan", "juan@gmail.com", "Calle 123")
cliente2 = Cliente("Maria", "maria@gmail.com", "Avenida 456")

producto1 = Producto("Camisa", 20)
producto2 = Producto("Pantalón", 30)
producto3 = Producto("Zapatos", 50)

cliente1.agregar_producto(producto1)
cliente1.agregar_producto(producto2)
cliente2.agregar_producto(producto3)

cliente1.eliminar_producto(producto2)

cliente1.realizar_compra()
cliente2.realizar_compra()