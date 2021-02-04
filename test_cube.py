import unittest
import cube

class TestCube(unittest.TestCase):
    def test_vol(self):
        self.assertEqual(cube.vol(3), 27)

    def test_input(self):
        self.assertRaises(TypeError, cube.vol, True)

    def test_negative(self):
        self.assertRaises(ValueError)

if __name__ == "__main__":
    unittest.main(verbosity=2)