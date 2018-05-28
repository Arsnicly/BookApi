import turtle as t
t.color ('blue')
t.shape ('turtle')
t.speed (3)

def drawsquare():
    for x in range(4):
        t.fd(90)
        t.left(90)


drawsquare()
