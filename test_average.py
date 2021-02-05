import unittest
import average

class TestAvg(unittest.TestCase):
    def test_avg(self):
        self.assertEqual(average.avg([2,3,4,5]), 3.5)

    def test_empty(self):
        self.assertRaises(ValueError)

    def test_input(self):
        self.assertRaises(TypeError)

if __name__ == "__main__":
    unittest.main(verbosity=2)       