import graphics as g
p= g.GraphWin('Padi B',1000,1000) #initialize the graphics window


class rectangle:
    def __init__(self, p1,p2):
        self.p1 = p1
        self.p2 = p2
        self.height = p1.y - p2.y
        self.width = p1.x - p2.x
        r = g.Rectangle(p1,p2)
        r.draw(p)
        

    def getArea(self):
        self.area = abs(self.height * self.width)
        return self.area

    def getPerimeter(self):
        self.perimeter = abs((self.height + self.width) * 2)
        return self.perimeter
        

    

def overlap(r1,r2):
    if((r1.p1.x > r2.p2.x) or (r2.p1.x > r1.p2.x)):
        return False

    if((r1.p1.y > r2.p2.y) or (r2.p1.y > r1.p2.y)):
        return False

    return True






        



