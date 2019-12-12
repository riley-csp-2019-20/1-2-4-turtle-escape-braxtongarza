#import turtle
import turtle as trtl
import random

#make a turtle
ted=trtl.Turtle()
player=trtl.Turtle()
ted.color="black"
ted.size=(3)
ted.shape="classic"
ted.speed(0)
player.color="red"

player.penup()
player.turtlesize(.5)
player.pencolor=("red")
player.shape('turtle')
player.goto(200,250)
player.pendown()


distance = 15
door_width = 20
wall_width = 10

def drawDoor():
    ted.penup()
    ted.forward(door_width)
    ted.pendown()

def drawBarrier():
     ted.right(90)
     ted.forward(20)
     ted.backward(20)
     ted.left(90)

#for or while loop to make the spiral
for i in range(40):
    if i > 4:
        door = random.randint(door_width ,distance - 2*door_width)
        barrier = random.randint( 2*wall_width , distance - 2*door_width)
        if door < barrier:
            ted.forward(door)
            drawDoor()
            ted.forward(barrier - door - door_width) 
            drawBarrier()
            ted.forward(distance - barrier)
        else:
            ted.forward(barrier)
            drawBarrier()
            ted.forward(door - barrier)
            drawDoor()
            ted.forward(distance - door - door_width)
        
    ted.left(90)
    distance += 10


def botup ():
    player.setheading(90)
    player.forward(10)
def botright ():
    player.setheading(0)
    player.forward(10)
def botdown ():
    player.setheading(270)
    player.forward(10)
def botleft ():
    player.setheading(180)
    player.forward(10)



#turtle screen
wn=trtl.Screen()

wn.onkeypress(botup,"Up")
wn.onkeypress(botright,"Right")
wn.onkeypress(botdown,"Down")
wn.onkeypress(botleft,"Left")
wn.listen()

#mainloop
wn.mainloop()