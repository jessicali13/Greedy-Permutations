from Greedy_Set import Point, WorkingSet
import Greedy_Permutation


class ChosenPoint:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

def setup():
    size(501, 501)
    frame.setResizable(True)
    global selected
    selected = []
        
        
def draw():
    fill(255)
    rect(0, 0, width, height)
    fill(0x000000)
    line(width / 2, 0, width / 2, height)
    line(0, height / 2, width, height / 2)
    
    for pt in selected:
        ellipse(pt.x, pt.y, 5, 5)
        
    text(str((mouseX - (width / 2) - 1) / 5) + " , " + str(-(mouseY - (height / 2)) / 5), 20, (height - 30))


def mousePressed():
    selected.append(ChosenPoint(mouseX, mouseY))