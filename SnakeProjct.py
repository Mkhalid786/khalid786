import turtle
import random
import time
founder="Mohammad Khalid"
delay=.5
score=0
highestscor=0

bodie=[]
s=turtle.Screen()
s.title("SNAKE GAME")
s.bgcolor("gray")
s.setup(width=600,height=600)

head=turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("white")
head.fillcolor("black")
head.penup()
head.goto(0,0)
head.direction="stop"

food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("black")
food.fillcolor("red")
food.penup()
food.ht()
food.goto(0,200)
food.st()

sb=turtle.Turtle()
sb.shape("circle")
sb.fillcolor("black")
sb.penup()
sb.ht()
sb.goto(-250,-250)
sb.write("Score :0 | heighestscore :0")

def moveup():
    if head.direction!="down":
        head.direction="up"
def movedown():
    if head.direction!="up":
        head.direction="down"
def moveleft():
    if head.direction!="right":
        head.direction="left"
def moveright():
    if head.direction!="left":
        head.direction="right"

def movestop():
    head.direction="stop"

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)

    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

s.listen()
s.onkey(moveup,"Up")
s.onkey(movedown,"Down")
s.onkey(moveleft,"Left")
s.onkey(moveright,"Right")
s.onkey(movestop,"space")

while True:
    s.update()
    if head.xcor()>290:
        head.setx(-290)

    if head.xcor()<-290:
        head.setx(290)

    if head.ycor()>290:
        head.sety(-290)


    if head.ycor()<-290:
        head.sety(290)

    if head.distance(food)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        body=turtle.Turtle()
        body.speed(10)
        body.penup()
        body.shape("square")
        body.color("red")
        body.fillcolor("black")
        bodie.append(body)

        score+=10
        delay=0.1

        if score>highestscor:
            highestscor=score
        sb.clear()
        sb.write("Score : {} Highest Score : {} \n\n Founder: {}".format(score,highestscor,founder))
        


    for index in range(len(bodie)-1,0,-1):
        x=bodie[index-1].xcor()
        y=bodie[index-1].ycor()
        bodie[index].goto(x,y)

    if len(bodie)>0:
        x=head.xcor()
        y=head.ycor()
        bodie[0].goto(x,y)
    move()

    for body in bodie:
        if body.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
           

            for body in bodie:
                body.ht()
            bodie.clear()
            score=0
            delay=0.1

            sb.clear()
            sb.write("Score :{} HighestScore :{}".format(score, highestscor))
    time.sleep(delay)
s.mainloop()
