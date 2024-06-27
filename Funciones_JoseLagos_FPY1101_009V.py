import os
import datetime
os.system("cls")


libros = []



def menu():
    while True:
        try:
            print("* * * MENÚ * * *")
            print(f"1. Registrar libro\n2. Prestar libro\n3. Listar todos los libros\n4. Imprimir reporte de préstamos\n5. Salir del Programa")
            op = int(input("Seleccione una opción del menu: "))
        except ValueError:
            print("Dato ingresado es erróneo")
            continue
        if op == 1:
            registro()
        elif op == 2:
            prestar()
        elif op == 3:
            listar()
        elif op == 4:
            imprimir()
        elif op == 5:
            print("Programa finalizado...")
            print("Desarrollado por José Lagos")
            print("RUN: 18.481.163-4")
            break
        else:
            print("Opción ingresada no existe")

def registro(): #Título, Autor, Año de Publicación, SKU.
    try:
        titulo = input("Ingrese el título del libro: ")
        tituloarreglo = [titulo]
        autor = input("Ingrese el autor del libro: ")
        autorarreglo = [autor]
        añopub = input("Ingrese año de publicación: ")
        prestado = False
        fecha_prestamo = ""
        nombre_usuario = ""
        if titulo == "" or autor =="" or añopub == "":
            print("Existen datos faltantes")
        else:
            for letratit in tituloarreglo:
                tit1 = (letratit[0]+ letratit[1]+ letratit[2] + letratit[3] + letratit[4] + letratit[5])
            for letraaut in autorarreglo:
                aut1 = (letraaut[0]+ letraaut[1]+ letraaut[2])
            
            sku = (tit1+ "-" + aut1 + "-"+ añopub)

            libro = {
                'Título': titulo,
                'Autor': autor,
                'Año de publicación': añopub,
                'SKU': sku,
                'Prestado' : prestado,
                'Fecha Prestamo' :  fecha_prestamo,
                'Usuario' : nombre_usuario 
            }
            libros.append(libro)
            print("Registro de libro fue un éxito")
    except ValueError:
        print("Debe ingresar un año válido")

def prestar():
    nombredeusuario = input("Ingrese nombre de usuario: ")
    skuconsulta = input("Ingrese SKU del libro a consultar: ")

    if skuconsulta == libros['SKU'] and libros['Prestado'] == False:
        print("Libro disponible para prestar")
        for skuconsulta in libros['SKU']:
            skuconsulta['Usuario'] = nombredeusuario
            skuconsulta['Fecha Prestamo'] = datetime.time()
        
    else:
        print("Libro no se encuentra disponible")

def listar():
    print(f"Titulo\t\tAutor\t\tAño de publicación\t\tSKU\t\tPrestado\n")
    for libro in libros:
        print(f"{libro['Título']}\t\t{libro['Autor']}\t\t{libro['Año de publicación']}\t\t{libro['SKU']}\t\t{libro['Prestado']}")

'''def imprimir():
        with open('Listado libros prestados.txt','w') as archivo:
           # archivo.write({libros['Título']}\t\t{libros['Autor']}\t\t{libros['Año de publicación']}\t\t{libros['SKU']}\t\t{libros['Prestado']})
    
'''




