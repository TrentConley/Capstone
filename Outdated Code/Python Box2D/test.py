import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("bouncing balls")

ball = turtle.Turtle()
ball.shape("circle")
ball.color("green")
ball.penup()
ball.speed(0)

ball.goto(0, 200)







wn.mainloop()
