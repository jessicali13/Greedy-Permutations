import math
import unittest


class Point:
    """Class for points defined by their coordinates in 2-D space"""

    def __init__(self, init_x, init_y):
        self.x = init_x
        self.y = init_y
        self.wset_dist = -1

    def pointdistance(self, targetpoint):
        """
        Computes the distance between current point and target point.
        :param targetpoint:
        :return: The distance between targetpoint and self
        """

        returndist = math.sqrt(((self.x - targetpoint.x) ** 2) + ((self.y - targetpoint.y) ** 2))
        return returndist

    def wsetdistance(self, workingset):
        """
        Computes the smallest distance between current point and greedy working set
        then sets the current point's wset_dist to that distance.
        :param workingset:
        :return: The distance between the workingset and self
        """

        smallestdistance = float('inf')

        for workingpoint in workingset.set:
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

    def addpoint(self, targetpoint):
        """
        Appends the target point to the end of the workingset and increments the set size
        then increments the set size counter
        :param targetpoint:
        """

        self.set.append(targetpoint)
        self.setsize += 1

    def removepoint(self, targetpoint):
        """
        Removes the target point and decrements the set size counter
        :param targetpoint:
        """
        self.setsize -= 1
        self.set.remove(targetpoint)


class TestGreedySet(unittest.TestCase):
    """Test class for the file"""

    # This is the test case for the functions of Point class
    def test_point(self):
        testingset = [Point(0, 2), Point(2, 0), Point(1, 1)]
        testwset = WorkingSet()
        for a in testingset:
            testwset.addpoint(a)

        testingpoint = Point(0, 0)

        self.assertEqual(testingpoint.pointdistance(testingset[0]), 2)
        self.assertEqual(testingpoint.pointdistance(testingset[1]), 2)
        self.assertEqual(testingpoint.pointdistance(testingset[2]), math.sqrt(2))
        self.assertEqual(testingpoint.wsetdistance(testwset), math.sqrt(2))

    # This is the test case for the functions of WorkingSet class
    def test_workingset(self):
        testwset = WorkingSet()
        self.assertEqual(testwset.setsize, 0)

        testinglist = [Point(0, 2), Point(2, 0), Point(1, 1), Point(0, 0)]
        for node in testinglist:
            testwset.addpoint(node)
        self.assertEqual(testwset.setsize, 4)

        testwset.removepoint(testinglist[0])
        self.assertEqual(testwset.setsize, 3)
        self.assertNotEqual(testwset.set[0], testinglist[0])

        testwset.removepoint(testinglist[1])
        self.assertEqual(testwset.setsize, 2)
        self.assertNotEqual(testwset.set[0], testinglist[1])


if __name__ == '__main__':
    unittest.main()