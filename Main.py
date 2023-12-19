from compras.Cliente import Cliente
from compras.Producto import Producto

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