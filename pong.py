#Let's try to make pong together!!!!!!!!
#This is soo cool
import turtle

ycord1 = -110
ycord2 = -150


#Set up the screen
def createBoard(bob,gameScreen,player1,player2,ball):
    #gameScreen.title("PONG")
    bob.ht()
    #Draw Box
    bob.speed(0)
    bob.penup()
    bob.pencolor("Black")
    bob.goto(-480,-350)
    bob.pendown()
    for i in range(2):
        bob.forward(960)
        bob.left(90)
        bob.forward(500)
        bob.left(90)
    #Write PONG
    bob.penup()
    bob.goto(-100,225)
    bob.pendown()
    bob.write("PONG",font=("Arial", 75, "normal"))
    #Draw Scoreboard
    #Create Pongs
    ball.speed(0)
    ball.shape("square")
    ball.penup()
    ball.goto(0,-100)

    player1.speed(0)
    player1.penup()
    player1.shape("square")
    player1.shapesize(5,1,None)
    player1.goto(-460,-100)

    player2.speed(0)
    player2.penup()
    player2.shape("square")
    player2.shapesize(5,1,None)
    player2.goto(460,-100)
    

def playGame(bob,gameScreen,player1,player2,ball):    
    gameScreen.onkey(player1.goto(-460,ycord1+2),"up")
    gameScreen.listen(None,None)


def main():
    bob = turtle.Turtle()
    player1 = turtle.Turtle()
    player2 = turtle.Turtle()
    ball = turtle.Turtle()
    gameScreen = turtle.setup(1000,750,startx=0,starty=0)
    
    createBoard(bob,gameScreen,player1,player2,ball)
    playGame(bob,gameScreen,player1,player2,ball)
    print("Hello World")

main()
