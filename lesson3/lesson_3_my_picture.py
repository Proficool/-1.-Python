from turtle import Screen, Turtle

def draw_piggy():
    # Установка параметров
    screen = Screen()
    screen.setup(width=1920, height=1080)
    screen.bgcolor("lightblue")

    piggy_turtle = Turtle()
    piggy_turtle.speed(2)
    piggy_turtle.shape("turtle")
    piggy_turtle.pensize(3)
    piggy_turtle.color("pink")

    # Мордочка
    piggy_turtle.penup()
    piggy_turtle.goto(250, -200)
    piggy_turtle.pendown()
    diameter = 180
    piggy_turtle.circle(diameter / 2)

    # Пяточок
    piggy_turtle.penup()
    piggy_turtle.goto(250, -150)
    piggy_turtle.pendown()
    diameter = 60
    piggy_turtle.circle(diameter / 2)

    # Ноздри
    piggy_turtle.penup()
    piggy_turtle.goto(235, -130)
    piggy_turtle.pendown()
    diameter = 10
    piggy_turtle.circle(diameter / 2)

    piggy_turtle.penup()
    piggy_turtle.goto(265, -130)
    piggy_turtle.pendown()
    piggy_turtle.circle(diameter / 2)

    # Глаза
    piggy_turtle.penup()
    piggy_turtle.goto(200, -80)
    piggy_turtle.pendown()
    piggy_turtle.setheading(35)
    piggy_turtle.forward(30)

    piggy_turtle.penup()
    piggy_turtle.goto(300, -80)
    piggy_turtle.pendown()
    piggy_turtle.setheading(145)
    piggy_turtle.forward(30)

    # Уши
    tilt_angle = 5  # Угол наклона

    # Левое ухо
    piggy_turtle.penup()
    piggy_turtle.goto(150, -95)
    piggy_turtle.pendown()
    piggy_turtle.setheading(60 - tilt_angle)
    piggy_turtle.forward(90)
    piggy_turtle.left(120)
    piggy_turtle.forward(90)
    piggy_turtle.left(120)
    piggy_turtle.forward(90)

    # Правое ухо
    piggy_turtle.penup()
    piggy_turtle.goto(350, -95)
    piggy_turtle.pendown()
    piggy_turtle.setheading(120 + tilt_angle)
    piggy_turtle.forward(90)
    piggy_turtle.right(120)
    piggy_turtle.forward(90)
    piggy_turtle.right(120)
    piggy_turtle.forward(90)

    piggy_turtle.hideturtle()

    # Закрытие окна при клике
    screen.exitonclick()

# Вызов функции для рисования
draw_piggy()
