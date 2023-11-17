import unittest
from main import is_cyclic

class TestCycleDetection(unittest.TestCase):

    def test_no_cycle(self):
        graph = {
            0: [1, 2],
            1: [0, 3],
            2: [0],
            3: [1, 4],
            4: [3]
        }
        self.assertFalse(is_cyclic(graph))


    def test_empty_graph(self):
        graph = {}
        self.assertFalse(is_cyclic(graph))

    def test_single_node(self):
        graph = {0: []}
        self.assertFalse(is_cyclic(graph))

    def test_self_cycle(self):
        graph = {
            0: [0]
        }
        self.assertTrue(is_cyclic(graph))

if __name__ == '__main__':
    unittest.main()


