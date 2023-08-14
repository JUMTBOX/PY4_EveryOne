import turtle as t
import random

t.bgcolor("black")
t.pencolor("yellow")
t.speed(1000)

for i in range(30):
    t.penup()
    x = random.randint(-350, 350)
    y = random.randint(-350, 350)
    starSize = random.randint(10, 30)
    t.goto(x, y)
    t.pendown()
    for i in range(5):
        t.forward(starSize)
        t.right(144)

t.mainloop()
