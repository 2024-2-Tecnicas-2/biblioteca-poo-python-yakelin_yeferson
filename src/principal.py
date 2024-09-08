
from revista import Revista
from libro import Libro

# Lista global para almacenar publicaciones
publicaciones = []

def sc():
    """Función de ayuda para leer entradas del usuario."""
    return input()

def agregar_publicacion(opc):
    if opc == 1:
        print("Ingrese el nombre de la revista: ")
        nombre = sc()
        print("Ingrese el año de publicación: ")
        ano = int(sc())
        print("Ingrese el número de revistas: ")
        numero_revistas = int(sc())
        print("Ingrese el nombre de la revista: ")
        nombre_revista = sc()

        rv = Revista(numero_revistas, nombre_revista, nombre, ano)
        publicaciones.append(rv)

    elif opc == 2:
        print("Ingrese el nombre del libro: ")
        nombre = sc()
        print("Ingrese el año de publicación: ")
        ano = int(sc())
        print("Ingrese el número de páginas: ")
        numero_paginas = int(sc())
        print("Ingrese el autor del libro: ")
        autor = sc()

        lb = Libro(autor, numero_paginas, nombre, ano)
        publicaciones.append(lb)

def mostrar_publicaciones():
    if len(publicaciones) == 0:
        print("No hay publicaciones.")
    else:
        for i, pub in enumerate(publicaciones):
            print(f"{i}. {pub}")

def editar_publicacion():
    mostrar_publicaciones()
    print("Ingrese el índice de la publicación que desea editar: ")
    index = int(sc())

    if index < 0 or index >= len(publicaciones):
        print("Índice inválido")
        return

    print("Ingrese el nuevo título: ")
    nuevo_titulo = sc()
    publicaciones[index].titulo = nuevo_titulo
    print("Publicación actualizada con éxito.")

if __name__ == '__main__':
    while True:
        print("1. Agregar publicación Revista")
        print("2. Agregar publicación Libro")
        print("3. Mostrar publicaciones")
        print("4. Editar publicación")
        print("5. Salir")

        opc = int(sc())

        if opc == 1 or opc == 2:
            agregar_publicacion(opc)
        elif opc == 3:
            mostrar_publicaciones()
        elif opc == 4:
            editar_publicacion()
        elif opc == 5:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
