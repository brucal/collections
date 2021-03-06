import unittest
from collection import Vector


class VectorTestCase(unittest.TestCase):
    def test_vector(self):
        vec = Vector()
        vec.add(1)
        self.assertTrue(vec.is_empty() is False)

    def test_vector_empty(self):
        vec = Vector()
        self.assertTrue(vec.is_empty())


if __name__ == '__main__':
    unittest.main()
