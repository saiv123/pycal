t = 0
s1 = int(input("length of the side 1?"))
s2 = int(input("length of the side 2?"))
s3 = int(input("length of the side 3?"))
s4 = int(input("length of the side 4?"))
co = input("what color do you want the Turtle?")
if co == "red" or "blue" or "green" or "gray" or "white" or "light blue" or "light green" or "light green" or "light gray" or "pink" or "yellow" or "orange" or "hot pink" or "navy":
    t = 5
else:
    print("Use the colors;red,green,gray,blue,white,light blue,light green,light gray,pink,yellow,orange,hot pink,navy")
import turtle
wn = turtle.Screen()
Fil = turtle.Turtle()
Fil.fillcolor(co)
Fil.shape("turtle")
Fil.speed(1)
Fil.forward(s1)
Fil.left(90)
Fil.circle(0)
Fil.forward(s2)
Fil.left(90)
Fil.circle(0)
Fil.forward(s3)
Fil.left(90)
Fil.circle(0)
Fil.forward(s4)
Fil.circle(0)
"""
name = input("what is your name?")
print('Hi '+ name) 
num = input("what is your name")
print("your age is " + num)
print("your name is " + name + " and you age is " + num)
"""
