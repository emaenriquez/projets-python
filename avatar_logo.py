from turtle import * 
speed(0)
bgcolor('black')
color('orange')
hideturtle()

radio=1
incremento=True

while True:
    circle(radio)
    if incremento:
        radio=radio-1
    else:
        radio=radio+1
    if radio==0 or radio==60:
        incremento = not incremento
    left(1)
    forward(3)