import turtle


def draw_square(side_length):
    for _ in range(4):
        turtle.forward(side_length)
        turtle.right(90)

def draw_cube():
    # Рисуем переднюю сторону
    draw_square(100)

    # Рисуем заднюю сторону
    turtle.penup()
    turtle.goto(50, 50)  # Перемещаемся в правый верхний угол
    turtle.pendown()
    draw_square(100)

    # Соединяем углы
    turtle.penup()
    turtle.goto(0, 0)  # Возвращаемся в начало
    turtle.pendown()
    turtle.goto(50, 50)

    turtle.penup()
    turtle.goto(100, 0)  # Перемещаемся в правый нижний угол
    turtle.pendown()
    turtle.goto(150, 50)

    turtle.penup()
    turtle.goto(0, 100)  # Перемещаемся в левый верхний угол
    turtle.pendown()
    turtle.goto(50, 150)

    turtle.penup()
    turtle.goto(100, 100)  # Перемещаемся в правый верхний угол
    turtle.pendown()
    turtle.goto(150, 150)


# Настройки черепашки
turtle.speed(1)  # Скорость рисования
turtle.pensize(2)  # Толщина линии это я сделал с помощью чата гпт

draw_cube()

turtle.done()  # Завершает работу черепашки