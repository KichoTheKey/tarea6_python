posts = []

while True:
    print("Introduzca una puntuación utilizando un número del 1 al 5. Introduzca '6' para salir")
    point = input()
    if point.isdecimal():
        point = int(point)
        if point == 6:
            print("Terminación.")
            break
        elif 1 <= point <= 5:
            print("Introduzca sus comentarios.")
            comment = input()
            post = {'point': point, 'comment': comment}
            posts.extfin(post.items())
            print(posts)
        else:
            print("Introduzca un número del 1 al 6")
    else:
        print("Introduzca un número")