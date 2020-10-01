import turtle
window = turtle.Screen()
turtle.reset()

turtle.shape('triangle')
turtle.bgcolor('#8D54FF')
turtle.color('black')

turtle.speed(9)
turtle.pensize(7)

turtle.circle(100)
turtle.color('white')
turtle.left(120)
turtle.forward(170)
turtle.right(120)
turtle.forward(170)
turtle.right(120)
turtle.forward(170)
window.exitonclick()
