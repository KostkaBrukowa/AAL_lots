import unittest

from src.models.PointsQueue import PointsQueue
from src.models.Side import Side


class MyTestCase(unittest.TestCase):
    def test_empty_queues(self):
        """when points_queue is passed an empty set it should have empty internal queues"""
        # given
        points_set = set()

        # given
        points_queue = PointsQueue(points_set)

        # then
        self.assertEqual(len(points_queue.vertical_queue), 0)
        self.assertEqual(len(points_queue.horizontal_queue), 0)

    def test_queues_length(self):
        """when passed a set with points, internal queues should have same number of element as set"""
        # given
        points_set = {(1, 1), (1, 2), (3, 1)}

        # when
        points_queue = PointsQueue(points_set)

        # then
        self.assertEqual(len(points_queue.vertical_queue), len(points_set))
        self.assertEqual(len(points_queue.horizontal_queue), len(points_set))

    def test_elements_position(self):
        """should return correct edge points when asked for farmost elements"""
        # given
        points_set = {(1, 10), (5, 2), (3, 0), (0, 9), (3, 3)}

        # when
        points_queue = PointsQueue(points_set)

        # then
        self.assertEqual(points_queue.get_edge_point(Side.LEFT), (0, 9))
        self.assertEqual(points_queue.get_edge_point(Side.RIGHT), (5, 2))
        self.assertEqual(points_queue.get_edge_point(Side.TOP), (1, 10))
        self.assertEqual(points_queue.get_edge_point(Side.BOTTOM), (3, 0))

    def test_elements_updates(self):
        """should return correct elements when points are removed from points_set"""
        # given
        points_set = {(1, 10), (5, 2), (3, 0), (0, 9), (3, 3)}

        # when
        points_queue = PointsQueue(points_set)
        points_set.remove((1, 10))

        # then
        self.assertEqual(points_queue.get_edge_point(Side.LEFT), (0, 9))
        self.assertEqual(points_queue.get_edge_point(Side.RIGHT), (5, 2))
        self.assertEqual(points_queue.get_edge_point(Side.TOP), (0, 9))
        self.assertEqual(points_queue.get_edge_point(Side.BOTTOM), (3, 0))

    def test_get_returning_none(self):
        """should return none when points set is emptied"""
        # given
        points_set = {(1, 10), (5, 2), (3, 0), (0, 9), (3, 3)}

        # when
        points_queue = PointsQueue(points_set)
        points_set.clear()

        # then
        self.assertEqual(points_queue.get_edge_point(Side.LEFT), None)
        self.assertEqual(points_queue.get_edge_point(Side.RIGHT), None)
        self.assertEqual(points_queue.get_edge_point(Side.TOP), None)
        self.assertEqual(points_queue.get_edge_point(Side.BOTTOM), None)

    def test_clear_correct_points(self):
        """should remove correct points when side is being cleared"""
        # given
        points_set = {(1, 10), (5, 2), (3, 0), (0, 9), (3, 10)}
        points_queue = PointsQueue(points_set)

        # when
        points_queue.clear_side(Side.TOP)

        # then
        self.assertTrue((1, 10) not in points_set)
        self.assertTrue((3, 10) not in points_set)
        self.assertEqual(len(points_set), 3)
        self.assertEqual(len(points_queue.vertical_queue), 3)

    def test_clear_correct_points_after_get(self):
        """should remove correct points when side is being cleared"""
        # given
        points_set = {(1, 10), (5, 2), (3, 0), (0, 9), (6, 10)}
        points_queue = PointsQueue(points_set)

        # when
        points_queue.clear_side(Side.TOP)
        points_queue.get_edge_point(Side.RIGHT)

        # then
        self.assertEqual(len(points_queue.horizontal_queue), 4)


if __name__ == '__main__':
    unittest.main()
