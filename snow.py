import turtle as t

#Snow Tree
#iATER Lab
#python
#By KHan

roo = t.Turtle()
wn = t.Screen()
wn.bgcolor("black")
wn.title("snow Tree partern")
roo.left(90)
roo.speed(1000)


def draw(l):
    if (l <  10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("yellow")
        roo.forward(l)
        roo.left(30)
        draw(3 *  l / 4)
        roo.right(60)
        draw(3 *  l / 4)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)

draw(20)
roo.right(90)
roo.speed(2000)

def draw(l):
    if(l < 10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("magenta")
        roo.forward(l)
        roo.left(30)
        draw(3 *  l / 4)
        roo.right(60)
        draw(3 *  l / 4)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)

draw(20)
roo.left(270)
roo.speed(2000)

def draw(l):
    if(l < 10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("red")
        roo.forward(l)
        roo.left(30)
        draw(3 *  l / 4)
        roo.right(60)
        draw(3 *  l / 4)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)

draw(20)
roo.right(90)
roo.speed(2000)

def draw(l):
    if(l < 10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("#fff8dc")
        roo.forward(l)
        roo.left(30)
        draw(3 *  l / 4)
        roo.right(60)
        draw(3 *  l / 4)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)

draw(20)

def draw(l):
    if(l < 10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("lightgreen")
        roo.forward(l)
        roo.left(30)
        draw(3 *  l / 5)
        roo.right(60)
        draw(3 *  l / 5)
        roo.left(30)
        roo.pensize(3)
        roo.backward(l)

draw(40)
roo.right(90)
roo.speed(2000)

def draw(l):
    if(l < 10):
        return
    else:
        roo.pensize(3)
        roo.pencolor("red")
        roo.forward(l)
        roo.left(30)
        draw(4 *  l / 5)
        roo.right(60)
        draw(4 *  l / 5)
        roo.left(30)
        roo.pensize(3)
        roo.backward(l)
        
draw(40)
roo.left(270)
roo.speed(2000)

def draw(l):
    if(l < 10):
        return
    else:
        roo.pensize(3)
        roo.pencolor("yellow")
        roo.forward(l)
        roo.left(30)
        draw(4 *  l / 5)
        roo.right(60)
        draw(4 *  l / 5)
        roo.left(30)
        roo.pensize(3)
        roo.backward(l)

draw(40)
roo.right(90)
roo.speed(2000)

def draw(l):
    if(l < 10):
        return
    else:
        roo.pensize(3)
        roo.pencolor("#fff8dc")
        roo.forward(l)
        roo.left(30)
        draw(4 *  l / 5)
        roo.right(60)
        draw(4 *  l / 5)
        roo.left(30)
        roo.pensize(3)
        roo.backward(l)

draw(40)

def draw(l):
    if(l < 10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("cyan")
        roo.forward(l)
        roo.left(30)
        draw(6 *  l / 7)
        roo.right(60)
        draw(6 *  l / 7)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)

draw(60)
roo.right(90)
roo.speed(2000)

def draw(l):
    if(l < 10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("yellow")
        roo.forward(l)
        roo.left(30)
        draw(6 *  l / 7)
        roo.right(60)
        draw(6 *  l / 7)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)


draw(60)
roo.left(270)
roo.speed(2000)

def draw(l):
    if(l < 10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("magenta")
        roo.forward(l)
        roo.left(30)
        draw(6 *  l / 7)
        roo.right(60)
        draw(6 *  l / 7)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)

draw(60)
roo.right(90)
roo.speed(2000)

def draw(l):
    if(l < 10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("#fff8dc")
        roo.forward(l)
        roo.left(30)
        draw(6 *  l / 7)
        roo.right(60)
        draw(6 *  l / 7)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)

draw(60)
wn.exitonclick()
