from math import prod
from typing import Dict, List

from servicios import *
from database.db import productos

menu = {1: 'LEER', 2: 'AGREGAR', 3: 'ACTUALIZAR', 4: 'BORRAR',
        5: 'PRODUCTO MAYOR PRECIO', 6: 'PRODUCTO MENOR PRECIO',
        7: 'PRECIO PROMEDIO', 8: 'VALOR TOTAL INVENTARIO',
        9: 'SALIR'}

def mostrar_menu(menu):    
    for num, opcion in menu.items():
        print(num, opcion)
         

def main():
    opcion = True
    
    db = productos

    while opcion:
        mostrar_menu(menu)
        opcion_seleccionada = int(input('Seleccione una opción para continuar '))
        
        # Leer producto o DB completa
        if opcion_seleccionada == 1:            
            opcion_lectura = input("Inserte un codigo de producto para consultar o presione Enter para mostrar todos ")
            codigo = opcion_lectura if opcion_lectura else None
            resultado = leer(db, codigo)
            print_dict(resultado)
        
        # Agregar Producto
        elif opcion_seleccionada == 2:
            nombre = input('Escriba el nombre del producto: ')
            precio = float(input('Escriba el precio del producto: '))
            cantidad = int(input('Escriba la cantidad del producto en el inventario: '))
            nuevo_producto = [nombre, precio, cantidad]
            agregar(db, nuevo_producto)
            print_dict(db)

        # Actualizar producto
        elif opcion_seleccionada == 3:
            codigo = int(input('Escriba el codigo del producto a actualizar: '))
            nombre = input('Escriba el nombre del producto: ')
            precio = float(input('Escriba el precio del producto: '))
            cantidad = int(input('Escriba la cantidad del producto en el inventario: '))
            producto_actualizado = {codigo: [nombre, precio, cantidad]}
            actualizar(db, producto_actualizado)
            print_dict(db)

        # Borrar producto
        elif opcion_seleccionada == 4:
            codigo = int(input('Escriba el codigo del producto a borrar: '))
            borrar(db, codigo)

        # Producto con mayor precio
        elif opcion_seleccionada == 5:
            resultado = producto_mayor_precio(db)
            print(resultado)
        
        # Producto con menor precio
        elif opcion_seleccionada == 6:
            resultado = producto_menor_precio(db)
            print(resultado)
        
        # Precio promedio
        elif opcion_seleccionada == 7:
            resultado = precio_promedio(db)
            print(resultado)

        # Valor total inventario
        elif opcion_seleccionada == 8:
            resultado = valor_total_inventario(db)
            print(resultado)
        
        # Salir
        elif opcion_seleccionada == 9:
            break

# main()
if __name__ == '__main__':
    main()


    

    