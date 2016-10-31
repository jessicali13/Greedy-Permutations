import math
import unittest


class Point:
    """Class for points defined by their coordinates in 2-D space"""

    def __init__(self, init_x, init_y):
        self.x = init_x
        self.y = init_y
        self.wset_dist = -1

    '''
    Computes the distance between current point and target point.
    @param1: Target point
    @return: Real number distance
    '''
    def pointdistance(self, targetpoint):
        returndist = math.sqrt(((self.x - targetpoint.x) ** 2) + ((self.y - targetpoint.y) ** 2))
        return returndist

    '''
    Computes the smallest distance between current point and greedy working set
    then sets the current point's wset_dist to that distance.
    @param1: Greedy working set, should be a list
    @return: Real number distance
    '''
    def wsetdistance(self, workingset):
        smallestdistance = float('inf')

        for workingpoint in workingset:
            tempdistance = self.pointdistance(workingpoint)
            if tempdistance < smallestdistance:
                smallestdistance = tempdistance

        self.wset_dist = smallestdistance
        return smallestdistance


class WorkingSet:
    """Class for the working set containing a list of points in the greedy permutation"""

    def __init__(self):
        self.set = []
        self.setsize = 0

    '''
    Appends the target point to the end of the workingset and increments the set size
    @param1: Target point
    '''
    def addpoint(self, targetpoint):
        self.set.append(targetpoint)
        self.setsize += 1

    '''
    Removes the point in the specified position and returns it
    @param1: Index number of the target point
    @return: Target point
    '''
    def removepoint(self, targetindex):
        self.setsize -= 1
        return self.set.pop(targetindex)


class TestGreedySet(unittest.TestCase):
    """Test class for the Point class functions"""

    # This is the test case for the functions of Point class
    def test_point(self):
        testingset = [Point(0, 2), Point(2, 0), Point(1, 1)]
        testingpoint = Point(0, 0)

        self.assertEqual(testingpoint.pointdistance(testingset[0]), 2)
        self.assertEqual(testingpoint.pointdistance(testingset[1]), 2)
        self.assertEqual(testingpoint.pointdistance(testingset[2]), math.sqrt(2))
        self.assertEqual(testingpoint.wsetdistance(testingset), math.sqrt(2))

    def test_workingset(self):
        testwset = WorkingSet()
        self.assertEqual(testwset.setsize, 0)

        testinglist = [Point(0, 2), Point(2, 0), Point(1, 1), Point(0, 0)]
        for node in testinglist:
            testwset.addpoint(node)
        self.assertEqual(testwset.setsize, 4)

        testingpoint = testwset.set[3]
        self.assertEqual(testwset.removepoint(3), testingpoint)
        testingpoint = testwset.set[0]
        self.assertEqual(testwset.removepoint(0), testingpoint)
        self.assertEqual(testwset.setsize, 2)


if __name__ == '__main__':
    unittest.main()