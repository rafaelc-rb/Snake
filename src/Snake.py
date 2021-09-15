import turtle
import time
import random

delay = 0.031

# Score
score = 0
high_score = 0

# Window
wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("black")
wn.setup(width=700, height=700)
wn.tracer(0) #turns off the screen updates

# Snake head creation
head = turtle.Turtle()
head.speed(0)
head.shape("triangle")
head.color("red")
head.penup()
head.goto(0,0)
head.shapesize(0.7,0.7,0.7)
head.direction = "stop"

# Sanke food
food = turtle.Turtle()
food.speed(0)
food.shape("turtle")
food.color("red")
food.penup()
food.goto(0,100)
food.shapesize(0.5,0.5,0.5)

# Snake Body
segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 305)
pen.write("Score: 0     High Score: 0", align="center", font=("ds-digital", 21, "normal"))

# Game limits
my_pen = turtle.Turtle()
my_pen.penup()
my_pen.shape("arrow")
my_pen.color("white")
my_pen.setposition(-300,-300)
my_pen.pendown()
my_pen.pensize(3)
for side in range(4):
    my_pen.forward(600)
    my_pen.left(90)
my_pen.hideturtle()

# Functions
def go_up():
    if head.direction != "down" and head.direction == "left":
        head.direction = "up"
        head.right(90)
    elif head.direction != "down" and head.direction == "right":
        head.direction = "up"
        head.left(90)
    elif head.direction == "stop":
        head.direction = "up"
        head.left(90)

def go_down():
    if head.direction != "up" and head.direction == "left":
        head.direction = "down"
        head.left(90)
    elif head.direction != "up" and head.direction == "right":
        head.direction = "down"
        head.right(90)
    elif head.direction == "stop":
        head.direction = "down"
        head.right(90)

def go_left():
    if head.direction != "right" and head.direction == "down":
        head.direction = "left"
        head.right(90)
    elif head.direction != "right" and head.direction == "up":
        head.direction = "left"
        head.left(90)
    elif head.direction == "stop":
        head.direction = "left"
        head.left(180)

def go_right():
    if head.direction != "left" and head.direction == "down":
        head.direction = "right"
        head.left(90)
    elif head.direction != "left" and head.direction == "up":
        head.direction = "right"
        head.right(90)
    elif head.direction == "stop":
        head.direction = "right"  

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 10)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 10)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 10)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 10)

def restoreheadposition():
    if head.direction == "up":
        head.right(90)
    elif head.direction == "down":
        head.left(90)
    elif head.direction == "left":
        head.left(180)

# Keyboard bidings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0,0)

        # Restore default position of the head
        restoreheadposition()

        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0
        pen.clear()
        pen.write("Score: {}     High Score: {}".format(score, high_score), align="center", font=("ds-digital", 21, "normal")) 

        # Reset the delay
        delay = 0.031
    
    # Check for a collision with a food
    if head.distance(food) <= 10:
        # Move the food to a random spot
        x = random.randint(-290, 280)
        y = random.randint(-280, 290)
        food.goto(x,y)

        # Add a body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("grey")
        new_segment.shapesize(0.5,0.5,0.5)
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        if delay > 0.01:
            delay -= 0.001
        elif delay <= 0.01:
            delay -= 0.0001

        # Increase the score
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}     High Score: {}".format(score, high_score), align="center", font=("ds-digital", 21, "normal")) 

    # Move the end segments fist in reverse order
    for index in range(len(segments) -1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    # Check for head collisions with the body segments
    for segment in segments:
        if segment.distance(head) < 10:
            time.sleep(1)
            head.goto(0,0)

            # Restore default position of the head
            restoreheadposition()

            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0
            pen.clear()
            pen.write("Score: {}     High Score: {}".format(score, high_score), align="center", font=("ds-digital", 21, "normal")) 

            # Reset the delay
            delay = 0.031

    time.sleep(delay)

wn.mainloop()
