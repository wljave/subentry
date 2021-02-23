import turtle

t = turtle.Turtle()
turtle.hideturtle()
t.speed(10)

def koch(x):
    if x <= 20:
        t.fd(x)
    else:
        x = x / 3
        koch(x)
        t.lt(60)
        koch(x)
        t.rt(120)
        koch(x)
        t.lt(60)
        koch(x)
        
for _ in range(3):
    koch(300)
    t.rt(120)
    
turtle.hideturtle()
turtle.done()
