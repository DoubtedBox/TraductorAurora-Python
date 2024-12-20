def main():
    # Programa de gestión de inventario

    # Declaración de listas
    codigos = [1001, 1002, 1003, 1004, 1005]
    nombres = ["Laptop", "Smartphone", "Tablet", "Monitor", "Teclado"]
    precios = [1200.50, 599.99, 349.75, 249.99, 79.50]
    existencias = [10, 25, 15, 20, 30]

    # Variable para el total de inventario
    total_inventario = 0.0

    # Calcular valor total del inventario
    for j in range(len(precios)):
        valor_producto = calcular_valor(precios[j], existencias[j])
        total_inventario += valor_producto

    # Encontrar el producto más caro
    producto_mas_caro = encontrar_producto_mas_caro(nombres, precios)

    # Imprimir resumen de inventario
    print("--- Resumen de Inventario ---")
    
    for i in range(len(nombres)):
        print(f"Producto: {nombres[i]}")
        print(f"Código: {codigos[i]} (Raíz cuadrada: {codigos[i] ** 0.5:.2f})")
        print(f"Precio: {precios[i]}")
        print(f"Existencias: {existencias[i]}")
        print(f"Valor Total: {calcular_valor(precios[i], existencias[i]):.2f}")
        print("------------------------")

    # Mostrar información general
    print(f"Total valor de inventario: {total_inventario:.2f}")
    print(f"Producto más caro: {producto_mas_caro}")

    # Solicitar interacción del usuario
    codigo_buscar = int(input("Ingrese código de producto a buscar: "))

    # Buscar producto por código
    encontrado = False
    for k in range(len(codigos)):
        if codigos[k] == codigo_buscar:
            print("Producto encontrado:")
            print(f"Nombre: {nombres[k]}")
            print(f"Precio: {precios[k]}")
            print(f"Existencias: {existencias[k]}")
            encontrado = True
            break

    # Validar si se encontró el producto
    if not encontrado:
        print("Producto no encontrado")

def calcular_valor(precio, cantidad):
    """Función para calcular el valor total de un producto."""
    return precio * cantidad

def encontrar_producto_mas_caro(nombres_prod, precios_prod):
    """Función para encontrar el producto más caro."""
    indice = 0
    precio_max = precios_prod[0]

    for i in range(1, len(precios_prod)):
        if precios_prod[i] > precio_max:
            precio_max = precios_prod[i]
            indice = i

    return nombres_prod[indice]

if __name__ == "__main__":
    main()
