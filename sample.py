while True:
    print('Seleccione el proceso que desea aplicar')
    print('1: Ingresa calificación y comentario')
    print('2: Comprueba los resultados obtenidos hasta ahora')
    print('3: Fin')
    num = input()
    
    if num.isdecimal():
        num = int(num)
        if num == 1:
            print('Introduzca una puntuación en una escala del 1 al 5')
            puntos = input()
            if puntos.isdecimal():
                puntos = int(puntos)
                if puntos <= 0 or puntos > 5:
                    print('Debe estar en una esacala de 1 a 5')
                else:
                    print('Ingrese el comentario')
                    comentario = input()
                    post = f'Puntos: {puntos}. Comentario: {comentario}'
                    file_pc = open("data.txt", 'a')
                    file_pc.write(f'{post} \n')
                    file_pc.close()
            else:
                print('Debe ser un número del 1 al 5')
        elif num == 2:
            print('Resultados hasta la fecha')
            read_file = open("data.txt", "r")
            print(read_file.read())
            read_file.close()
        elif num == 3:
            print('Fin')
            break
        else:
            print('Introduzca un número del 1 al 3')
    else:
        print('Introduzca un número del 1 al 3')