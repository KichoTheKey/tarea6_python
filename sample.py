while True:
    puntuacion = input('Ingrese una puntuación del 1 a 5. (Presione "6" para salir): ')
    if '0' <= puntuacion <= '9':
        puntuacion = int(puntuacion)        
        if puntuacion == 6:
            print("Salir")
            break
        if 1 <= puntuacion <= 5:
            comentarios = input("Por favor, introduzca sus comentarios: ")
            print(f'Sus puntos: {puntuacion} Sus comentarios: {comentarios}')
        else:
            print("Por favor, introduzca un número válido entre 1 y 5")
    else:
        print("Por favor, introduzca un número")