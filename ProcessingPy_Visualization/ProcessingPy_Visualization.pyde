from Greedy_Set import Point, WorkingSet
from Greedy_Permutation import greedypermutation, user_createnewpoint


class ChosenPoint:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

def setup():
    size(501, 501)
    frame.setResizable(True)
    global pointlist, greedylist
    pointlist = WorkingSet()
    greedylist = WorkingSet()
        
        
def draw():
    fill(255)
    rect(0, 0, width, height)
    fill(0x000000)
    line(width / 2, 0, width / 2, height)
    line(0, height / 2, width + 1, height / 2)
    
    if greedylist.setsize < 1:
        for pt in pointlist.set:
            ellipse(pt.x, pt.y, 5, 5)
        
    text(str((mouseX - (width / 2) - 1) / 5) + " , " + str(-(mouseY - (height / 2)) / 5), 20, (height - 30))


def mousePressed():
    user_createnewpoint(mouseX, mouseY, pointlist)