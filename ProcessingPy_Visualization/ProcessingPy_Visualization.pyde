from Greedy_Set import Point, WorkingSet
from Greedy_Permutation import greedypermutation, findminset, unselectall, user_createnewpoint


def setup():
    size(501, 501)
    frame.setResizable(True)
    global pointlist, ksize
    pointlist = WorkingSet()
    ksize = int()
   
                     
def draw():
    # Set up the coordinate grid
    background(255)
    ksize = mouseX / 10
    findminset(ksize, pointlist)
    
    # Draw the encompassing circles
    fill(208, 60, 60)
    for ptg in pointlist.set:
        if ptg.selected is True:
            ellipse(ptg.vis_x, ptg.vis_y, ksize * 10, ksize * 10)
            
    fill(0)
    # These lines are for reference only, sometimes it does not properly reflect the origin
    line(width / 2, 0, width / 2, height)
    line(0, height / 2, width + 1, height / 2)
    
    # Draw out all user defined points
    for pt in pointlist.set:
        ellipse(pt.vis_x, pt.vis_y, 5, 5)
        
    # Text box to display coordinates of current mouse location
    text(str((mouseX - (width / 2) - 1) / 5) + " , " + str(-(mouseY - (height / 2)) / 5), 20, (height - 30))
    text("k = " + str(mouseX / 10), 20, (height - 10))


def mousePressed():
    user_createnewpoint((mouseX - (width / 2) - 1) / 5, -(mouseY - (height / 2)) / 5, mouseX, mouseY, pointlist)
    unselectall(pointlist)
    greedylist = WorkingSet()
    greedypermutation(pointlist, greedylist)
    pointlist.set = greedylist.set
    pointlist.setsize = greedylist.setsize