import unittest
from tree import Tree

class TestFind(unittest.TestCase):

    def setUp(self):
        self.tree = Tree()
        for val in [5, 3, 7, 1, 4, 6, 8]:
            self.tree.add(val)

    def test_find_existing_node(self):
        node = self.tree.find(4)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 4)

    def test_find_root(self):
        node = self.tree.find(5)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 5)

    def test_find_nonexistent_node(self):
        node = self.tree.find(99)
        self.assertIsNone(node)

    def test_find_in_empty_tree(self):
        empty_tree = Tree()
        node = empty_tree.find(5)
        self.assertIsNone(node)

    def test_find_leaf_node(self):
        node = self.tree.find(1)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 1)


if __name__ == '__main__':
    unittest.main()
