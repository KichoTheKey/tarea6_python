def ingresar_calificacion():
    print('Introduzca una puntuación en una escala del 1 al 5')
    puntos = input()
    if puntos.isdecimal():
        puntos = int(puntos)
        if puntos <= 0 or puntos > 5:
            print('Debe estar en una escala de 1 a 5')
        else:
            print('Ingrese el comentario')
            comentario = input()
            post = f'Puntos: {puntos}. Comentario: {comentario}'
            with open("data.txt", 'a') as file_pc:
                file_pc.write(f'{post}\n')
    else:
        print('Debe ser un número del 1 al 5')

def comprobar_resultados():
    print('Resultados hasta la fecha')
    with open("data.txt", "r") as read_file:
        contenido = read_file.read()
        if contenido:
            print(contenido)
        else:
            print("Todavía no hay resultados disponibles")

while True:
    print('Seleccione el proceso que desea aplicar')
    print('1: Ingresa calificación y comentario')
    print('2: Comprueba los resultados obtenidos hasta ahora')
    print('3: Fin')
    num = input()
        
    if num.isdecimal():
        num = int(num)
        if num == 1:
            ingresar_calificacion()
        elif num == 2:
            comprobar_resultados()
        elif num == 3:
            print('Fin')
            break
        else:
            print('Introduzca un número del 1 al 3')
    else:
        print('Introduzca un número del 1 al 3')
