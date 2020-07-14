import turtle
import time
#creating the game screen
UwU = turtle.Screen()
UwU.title("Pong by Matthew")
UwU.bgcolor("black")
UwU.setup(width=800, height=600)
UwU.tracer(0)

#score
scorea = 0
scoreb = 0
#paddle a
paddlea = turtle.Turtle()
paddlea.speed(0)
paddlea.shape("square")
paddlea.shapesize(stretch_len=1, stretch_wid=5)
paddlea.color("white")
paddlea.penup()
paddlea.goto(-350,0)

#paddle b
paddleb = turtle.Turtle()
paddleb.speed(0)
paddleb.shape("square")
paddleb.shapesize(stretch_len=1, stretch_wid=5)
paddleb.color("white")
paddleb.penup()
paddleb.goto(350,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.5
ball.dy = 0.5

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player 1: 0    Player 2: 0 ", align="center", font=("Courier", 24, "normal"))

#Function
def paddlea_up():
    y = paddlea.ycor()
    y += 20
    paddlea.sety(y)

def paddlea_down():
     y = paddlea.ycor()
     y -= 20
     paddlea.sety(y)


def paddleb_up():
    y = paddleb.ycor()
    y += 20
    paddleb.sety(y)

def paddleb_down():
    y = paddleb.ycor()
    y -= 20
    paddleb.sety(y)

#Keyboard Binds
UwU.listen()
UwU.onkeypress(paddlea_up, "w")
UwU.onkeypress(paddlea_down, "s")
UwU.onkeypress(paddleb_up, "Up")
UwU.onkeypress(paddleb_down, "Down")

#game loop
while True:
    UwU.update()
    #Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        scorea +=1
        pen.clear()
        pen.write("Player 1: {}   Player 2: {}".format(scorea, scoreb), align="center", font=("Courier", 24, "normal"))
        time.sleep(0.7)
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        scoreb +=1
        pen.clear()
        pen.write("Player 1: {}   Player 2: {}".format(scorea, scoreb), align="center", font=("Courier", 24, "normal"))
        time.sleep(0.7)
    #paddle ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleb.ycor() + 40 and ball.ycor() > paddleb.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddlea.ycor() + 40 and ball.ycor() > paddlea.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1