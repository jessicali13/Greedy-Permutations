from Greedy_Set import Point, WorkingSet
import unittest


def greedypermutation(pointlist, greedyset):
    """
    The greedy permutation algorithm, takes WorkingSet of unselected points and outputs sorted WorkingSet
    :param pointlist: The list of unsorted points
    :param greedyset: The list of sorted points
    :return: The completed list ordered by greedy permutation
    """

    if pointlist.setsize < 1:
        # Return none if list of unselected points is empty
        return None

    # Choose the first point generated by user as the starting point
    greedyset.addpoint(pointlist.set[0])
    pointlist.removepoint(pointlist.set[0])

    # Compute inital distances from set
    for freepoint in pointlist.set:
        freepoint.wsetdistance(greedyset)

    # Begin inserting the rest of the points into the greedy set w/ greedy algorithm (furthest point from set)
    pointholder = None
    while pointlist.setsize > 0:
        tempdistance = 0
        for freepoint in pointlist.set:
            # Check if current freepoint is further from the set then current pointholder
            if freepoint.wset_dist > tempdistance:
                pointholder = freepoint
                tempdistance = freepoint.wset_dist

        # Insert furthest point into greedy set, remove from the list of unselected points
        greedyset.addpoint(pointholder)
        pointlist.removepoint(pointholder)

        # Updates all of the working set distances of the unselected points
        # w/ respect to the new entry in the greedy set
        for freepoint in pointlist.set:
            if freepoint.wset_dist > freepoint.pointdistance(pointholder):
                freepoint.wset_dist = freepoint.pointdistance(pointholder)

    return greedyset


def unselectall(greedyset):
    """
    Unselects all the points in the given greedy set
    :param greedyset: The target greedy set
    """

    for pt in greedyset.set:
        pt.selected = None


def findminset(radius, greedyset):
    """
    Select the minimum number of sorted points such that circles with the given radius
    can encompass all other points of the set
    :param radius: The user defined radius
    :param greedyset: The list of sorted points
    """

    templist = WorkingSet()
    for pt in greedyset.set:
        templist.addpoint(pt)

    unselectall(templist)

    for pt in templist.set:
        if pt.selected is None:
            pt.selected = True

            for spt in templist.set:
                if pt.pointdistance(spt) <= radius and spt.selected is None:
                    spt.selected = False


def user_createnewpoint(x, y, gridx, gridy, pointlist):
    """
    Takes user coordinate inputs and creates an instance of Point
    then inserts the instance into the list of unselected points
    :param x: x-coordinate
    :param y: y-coordinate
    :param gridx: x-coordinate of where the dot will be drawn
    :param gridy: y-coordinate of where the dot will be drawn
    :param pointlist:
    """

    newpoint = Point(x, y, gridx, gridy)
    pointlist.addpoint(newpoint)


class TestGreedyPermutation(unittest.TestCase):
    """Testing class for the file"""

    # Test case for greedy permutation algorithm
    def test_greedypermutation(self):
        alist = ([Point(-8, 0, 0, 0), Point(1, 0, 0, 0), Point(3, 8, 0, 0), Point(2, 2, 0, 0), Point(1, 9, 0, 0),
                  Point(-1, -4, 0, 0), Point(0, 0, 0, 0)])
        correctlist = [alist[0], alist[2], alist[1], alist[5], alist[3], alist[4], alist[6]]
        greedyset = WorkingSet()
        pointlist = WorkingSet()
        for a in alist:
            pointlist.addpoint(a)

        greedypermutation(pointlist, greedyset)
        for index, point in enumerate(greedyset.set):
            print str(greedyset.set[index].wset_dist)
            self.assertEqual(greedyset.set[index], correctlist[index])

    # Test case for findminset function
    def test_findminset(self):
        alist = ([Point(-8, 0, 0, 0), Point(1, 0, 0, 0), Point(3, 8, 0, 0), Point(2, 2, 0, 0), Point(1, 9, 0, 0),
                  Point(-1, -4, 0, 0), Point(0, 0, 0, 0)])
        k = 5
        pointlist = WorkingSet()
        greedylist = WorkingSet()
        for a in alist:
            pointlist.addpoint(a)

        greedypermutation(pointlist, greedylist)
        findminset(k, greedylist)

        # PLACEHOLDER TEST CASE || NOT COMPLETE

    # Test case for the unselectall function
    def test_unselectall(self):
        alist = ([Point(-8, 0, 0, 0), Point(1, 0, 0, 0), Point(3, 8, 0, 0), Point(2, 2, 0, 0), Point(1, 9, 0, 0),
                  Point(-1, -4, 0, 0), Point(0, 0, 0, 0)])
        pointlist = WorkingSet()
        for a in alist:
            pointlist.addpoint(a)
            a.selected = True

        for pt in pointlist.set:
            self.assertEqual(pt.selected, True)

        unselectall(pointlist)

        for pt in pointlist.set:
            self.assertEqual(pt.selected, None)

if __name__ == '__main__':
    unittest.main()