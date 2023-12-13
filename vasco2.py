from graphics import *
import random

CoordUltimaVar = Point(10, 10)

def ResetCoordUltimaVar():
    global CoordUltimaVar
    CoordUltimaVar = Point(10,10)

def ResetCoordUltimaVar():
    global CoordUltimaVar
    CoordUltimaVar = Point(10,10)

def TransferItemFromWinToWin(winA, winB):
    for item in winA.items[:]:
        item.undraw()
        item.draw(winB)

def ClearWindow(win):
    CoordUltimaVar = Point(10, 10)
    for item in win.items[:]:
        item.undraw()
    win.update()


def SelectRandColor():
    colors = ["red", "yellow", "green", "blue", "brown", "purple"]
    return random.choice(colors)

def CompareX(a,b):
    if(a.getX() > b.getX()):
        return a
    else:
        return b
    
def CompareY(a,b):
    if(a.getY() > b.getY()):
        temp = [a, b]
    else:
        temp = [b, a]
    return temp

def SetCoordinatesToDrawGate(x, y):
    
    BiggerX = CompareX(x,y)
    CoordX = BiggerX.getX()+ 200
    CoordY= (x.getY() + y.getY())/2
    PointMid = Point(CoordX, CoordY)
    
    PointInA = PointMid.clone()
    PointInA.move(0,-50)
    
    PointInB = PointMid.clone()
    PointInB.move(0,50)
    
    PointOut = PointMid.clone()
    PointOut.move(150,0)
    
    CoordPack = [PointMid, PointInA, PointInB, PointOut]
    
    return CoordPack

def DrawLines(win, CoordPack, x, y):
    temp = CompareY(x,y)
    lineA = Line(temp[0],CoordPack[2])
    lineB = Line(temp[1],CoordPack[1])
    lines = [lineA, lineB]
    lines

    return lines

def DrawNot(win, x):
    x.move(10,0)
    neg = Circle(x, 10)
    neg.draw(win)
    x.move(10,0)

    return x

def CreateAnd(CoordPack, x, y):
    Aux1 = CoordPack[1].clone()
    Aux1.move(110,0)
    Aux2 = CoordPack[2].clone()
    Aux2.move(110,0)
    Aux3 = CoordPack[3].clone()
    Aux3.move(-15,30)
    Aux4 = CoordPack[3].clone()
    Aux4.move(-15,-30)
    #semicirculo da frente
    
    Gate = Polygon( CoordPack[1],
                    CoordPack[2],
                    Aux2,
                    Aux3,
                    CoordPack[3],
                    Aux4,
                    Aux1
                    )
    Gate.setWidth(2)

    return Gate

def CreateOr(CoordPack, x, y):
    Aux1 = CoordPack[1].clone()
    Aux1.move(110,0)
    Aux2 = CoordPack[2].clone()
    Aux2.move(110,0)
    Aux3 = CoordPack[3].clone()
    Aux3.move(-15,30)
    Aux4 = CoordPack[3].clone()
    Aux4.move(-15,-30)
    #semicirculo da frente

    CoordPack[0].move(40,0)
    Aux6 = CoordPack[0].clone()
    Aux6.move(-15,30)
    Aux7 = CoordPack[0].clone()
    Aux7.move(-15,-30)
    #VAI SE FODER CAUAN
    Gate = Polygon( CoordPack[1],
                    Aux7,
                    CoordPack[0],
                    Aux6,
                    CoordPack[2],
                    Aux2,
                    Aux3,
                    CoordPack[3],
                    Aux4,
                    Aux1
                    )
    Gate.setWidth(2)

    return Gate

def DrawGate(win, x, gate, y):
    
    CoordPack = SetCoordinatesToDrawGate(x,y)
    Lines = DrawLines(win, CoordPack, x, y)
    Gate = ...

    if gate == "or":
        Gate = CreateOr(CoordPack, x, y)
    elif gate == "and":
        Gate = CreateAnd(CoordPack, x, y)
    
    Gate.draw(win)
    Lines[0].draw(win)
    Lines[1].draw(win)

    return CoordPack[3]

def DrawVar(win, name):
    x = CoordUltimaVar
    y = Point((CoordUltimaVar.getX() + 50), (CoordUltimaVar.getY() + 50))
    shape = Rectangle(x, y)
    shape.setFill(SelectRandColor())
    shape.setWidth(2)
    shape.draw(win)
    
    msg = Text(Point((CoordUltimaVar.getX() + 25), (CoordUltimaVar.getY() + 25)), name)
    msg.draw(win)
    CoordSaidaVar = Point((CoordUltimaVar.getX() + 50), (CoordUltimaVar.getY() + 25))
    CoordUltimaVar.move(0,100)

    return CoordSaidaVar


    (expr) and id


    #python D:\compiladores\main.py