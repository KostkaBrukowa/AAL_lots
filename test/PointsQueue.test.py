import unittest

from src.solutions.models.PointsQueue import PointsQueue
from src.solutions.models.Side import Side
from src.solutions.models.Square import Square

default_square = Square(0, 0, 0, 0)


class MyTestCase(unittest.TestCase):

    def test_empty_queues(self):
        """when points_queue is passed an empty set it should have empty internal queues"""
        # given
        points_set = set()

        # given
        points_queue = PointsQueue(default_square, points=points_set)

        # then
        self.assertEqual(len(points_queue.vertical_queue), 0)
        self.assertEqual(len(points_queue.horizontal_queue), 0)

    def test_queues_length(self):
        """when passed a set with points, internal queues should have same number of element as set"""
        # given
        points_set = {(1, 1), (1, 2), (3, 1)}

        # when
        points_queue = PointsQueue(default_square, points=points_set)

        # then
        self.assertEqual(len(points_queue.vertical_queue), len(points_set))
        self.assertEqual(len(points_queue.horizontal_queue), len(points_set))

    def test_elements_position(self):
        """should return correct edge points when asked for farmost elements"""
        # given
        points_set = {(2, 10), (5, 2), (3, 1), (1, 9), (3, 3)}
        square = Square(0, 10, 0, 11)

        # when
        points_queue = PointsQueue(square, points=points_set)

        # then
        self.assertEqual(points_queue.get_edge_point(Side.LEFT)[0], (1, 9))
        self.assertEqual(points_queue.get_edge_point(Side.RIGHT)[0], (5, 2))
        self.assertEqual(points_queue.get_edge_point(Side.TOP)[0], (2, 10))
        self.assertEqual(points_queue.get_edge_point(Side.BOTTOM)[0], (3, 1))

    def test_get_returning_none(self):
        """should return none when points set is emptied"""
        # given
        points_set = {(1, 10), (5, 2), (3, 0), (0, 9), (3, 3)}

        # when
        points_queue = PointsQueue(default_square, points=points_set)
        points_set.clear()

        # then
        self.assertEqual(points_queue.get_edge_point(Side.LEFT), None)
        self.assertEqual(points_queue.get_edge_point(Side.RIGHT), None)
        self.assertEqual(points_queue.get_edge_point(Side.TOP), None)
        self.assertEqual(points_queue.get_edge_point(Side.BOTTOM), None)


if __name__ == '__main__':
    unittest.main()
