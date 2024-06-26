import os

libros = []
prestamos = []

def registrar():
    try:
        user = input("Ingrese su nombre de usuario: ")
        book_title = input("Ingrese el nombre del libro: ")
        author = input("Ingrese el nombre del autor: ")
        book_date = int(input("Ingrese el año de Publicacion: "))
        sku = input("Ingrese el SKU: ")
        if book_title == "" or author == "" or book_date == None or sku == None:
            print("Datos faltantes o invalidos intente de nuevo.")
        else:
            libro = {
                "Usuario" : user,
                "Nombre" : book_title,
                "Autor" : author,
                "Año de publicacion" : book_date,
                "SKU" : sku
            }
            print("Datos guardados correctamente.")
            libros.append(libro)
    except ValueError:
        print("ERROR: Datos incorrectos")

def prestar():
    try:
        user = input("Ingrese su nombre de usuario: ")
        libro_p = input("Ingrese nombre del libro a prestar: ")
        autor_p = input("Ingrese el nombre del Autor: ")
        date_p = input("Ingrese la fecha de publicacion: ")
        sku_p = input("Ingrese el SKU del libro: ")
        if libro_p == "" or autor_p == "" or date_p == None or sku_p == None:
            print("Datos faltantes o invalidos intente de nuevo.")
        else:
            prestamo = {
                "Usuario" : user,
                "Nombre" : libro_p
            }
            print("Datos guardados correctamente.")
            prestamos.append(prestamo)
    except ValueError:
        print("ERROR: Datos incorrectos")

def listar():
    print("TÍTULO\t\tAUTOR\t\tAÑO DE PUBLICACIÓN\t\tSKU")
    for libro in libros:
        print(f"{libro["Nombre"]}\t\t{libro["Autor"]}\t\t{libro["Año de publicacion"]}\t\t\t{libro["SKU"]}")

def imprimir():
    try:
        print("-------------\n1. Imprimir\n2. Cancelar\n-------------")
        op = int(input("Que desea hacer?: "))
        if op == 1:
            with open ("Reporte_de_prestamos.txt", "w") as file:
                file.write("USUARIO\t\t\t TITULO\t\t\t FECHA DEL PRESTAMO")
            for libro in libros:
                file.write(f"{libro["Usuario"]}\t\t\t{libro["Nombre"]}")
            print("Archivo guardado en", os.getcwd())
        elif op == 2:
            menu()
    except ValueError:
        print("ERROR: Respuesta invalida, intente de nuevo.")


def menu():
    while True:
        try:
            print("-~-~-~-~MENÚ BIBLIOTECA~-~-~-~-\n 1. Registrar libro\n 2. Prestar libro \n 3. Listar todos los libros \n 4. Imprimir reporte de préstamos \n 5. Salir del Programa")
            op = int(input("Eliga una opcion del 1 al 5: "))
        except ValueError:
            print("ERROR: Opcion invalida")
        if op == 1:
            registrar()
        elif op == 2:
            prestar()
        elif op == 3:
            listar()
        elif op == 4:
            imprimir()
        elif op == 5:
            print(" Programa finalizado...\n Desarrollado por Mirko Lucic\n RUN: 21.392.043-K")
            break
        else: 
            print("ERROR: Opcion invalida")
