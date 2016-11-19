from Greedy_Set import Point, WorkingSet
from Greedy_Permutation import greedypermutation, findminpoints, user_createnewpoint


def setup():
    size(501, 501)
    frame.setResizable(True)
    global pointlist, greedylist
    pointlist = WorkingSet()
    greedylist = WorkingSet()
        
        
def draw():
    # Set up the coordinate grid
    fill(255)
    rect(0, 0, width, height)
    fill(0x000000)
    # These lines are for reference only, sometimes it does not properly reflect the origin
    line(width / 2, 0, width / 2, height)
    line(0, height / 2, width + 1, height / 2)
    
    # Draw out all user defined points
    for pt in pointlist.set:
        ellipse(pt.vis_x, pt.vis_y, 5, 5)
        
    # Text box to display coordinates of current mouse location
    text(str((mouseX - (width / 2) - 1) / 5) + " , " + str(-(mouseY - (height / 2)) / 5), 20, (height - 30))


def mousePressed():
    user_createnewpoint((mouseX - (width / 2) - 1) / 5, -(mouseY - (height / 2)) / 5, mouseX, mouseY, pointlist)