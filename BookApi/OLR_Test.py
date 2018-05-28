import turtle as t
#t.color ('darkkhaki')
t.colormode(255)
t.pencolor(21, 95, 30)
t.shape ('turtle')
t.speed (3)

def drawplus():
    for x in range(4):
        t.fd(90)
        t.left(90)
        t.fd(90)
        t.right(90)
        t.fd(90)
        t.left(90)


drawplus()
