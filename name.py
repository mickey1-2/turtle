import turtle
turtle.Screen().bgcolor("white")
sc=turtle.Screen()
sc.setup(400,300)
turtle.title("Welcome to the Turtle Window")
board=turtle.Turtle()
for i in range(4):
    board.forward(100)
    board.left(90)
    i=i+1