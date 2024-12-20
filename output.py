import math 

 # Traducción automática

def main():
    codigos = [1001,1002,1003,1004,1005]
    nombres = ["Laptop","Smartphone","Tablet","Monitor","Teclado"]
    precios = [1200.50,599.99,349.75,249.99,79.50]
    existencias = [10,25,15,20,30]
    prueba = True
    pozole = []
    pozole = [[1,2],[1,3,4]]
    total_inventario = 0.0
    total_inventario = 0.0
    j = 0
    while j < 5:
        valor_producto = calcular_valor(precios[j],existencias[j])
        total_inventario = total_inventario+valor_producto
        j = j+1

    producto_mas_caro = encontrar_producto_mas_caro(nombres,precios)
    print(f'--- Resumen de Inventario ---')
    for i in range(0, 4 + 1, 1):
        print(f'Producto:  {nombres[i]}')
        print(f'Código:  {math.sqrt(codigos[i]*codigos[i])}')
        print(f'Precio:  {precios[i]}')
        print(f'Existencias:  {existencias[i]}')
        print(f'Valor Total:  {calcular_valor(precios[i],existencias[i])}')
        print(f'------------------------')

    print(f'Total valor de inventario:  {total_inventario}')
    print(f'Producto más caro:  {producto_mas_caro}')
    nombre = ""
    print(f'Ingrese su nombre porfavor:')
    nombre = input()
    codigo_buscar = 1004.0
    print(f'Buscando producto con el codigo:  {codigo_buscar}')
    encontrado = False
    for k in range(0, 4 + 1, 1):
        if codigos[k] == codigo_buscar:
            print(f'---------------------------')
            print(f'Felicidades  {nombre} .')
            print(f'Producto encontrado:')
            print(f'Nombre:  {nombres[k]}')
            print(f'Precio:  {precios[k]}')
            print(f'Existencias:  {existencias[k]}')
            encontrado = True


    if encontrado == False:
        print(f'Producto no encontrado')

def calcular_valor(precio, cantidad):
        valor = precio*cantidad
        return valor;
def encontrar_producto_mas_caro(nombres_prod, precios_prod):
        indice = 0
        precio_max = precios_prod[0]
        i = 1
        while i < 5:
            if precios_prod[i] > precio_max:
                precio_max = precios_prod[i]
                indice = i

            i = i+1

        return nombres_prod[indice];


if __name__ == '__main__':
    main()
