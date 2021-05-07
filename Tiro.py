from random import randrange
from turtle import *
from freegames import vector
#Se importan las librerías necesarias


ball = vector(-200, -200)
speed = vector(0, 0)
targets = []
#Se definen las listas, y vectores necesarios


def tap(x, y): #funcion para colocar el clic dentro de los límites del tablero en caso de que se haya hecho afuera
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25


def inside(xy): #Funcion que evalua la posición del clic dentro de los límites del tablero
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw(): #funcion que dibuja los objetivos y la pelota lanzada
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


def move(): #funcion que da movimiento a los objetivos y a la pelota
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 1 #velocidad de los objetivos

    if inside(ball):
        speed.y -= 0.85 #velocidad del proyectil
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            return

    ontimer(move, 50)


setup(420, 420, 370, 0) #tamaño del tablero
hideturtle() #ocultar el cursor

up()
tracer(False)
onscreenclick(tap)
move()
done()
