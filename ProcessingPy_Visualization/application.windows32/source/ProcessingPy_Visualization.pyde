class ChosenPoint:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

def setup():
    size(1001, 1001)
    global selected
    selected = []
        
        
def draw():
    fill(255)
    rect(0, 0, width, height)
    fill(0x000000)
    line(501, 0, 501, 1001)
    line(0, 501, 1001, 501)
    for pt in selected:
        ellipse(pt.x, pt.y, 10, 10)
    text(str((mouseX - 501) / 10) + " , " + str((mouseY - 501) / 10), mouseX, mouseY)


def mousePressed():
    selected.append(ChosenPoint(mouseX, mouseY))