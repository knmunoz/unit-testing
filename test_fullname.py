import unittest
import fullname

class TestFullName(unittest.TestCase):
    def test_fullname(self):
        self.assertEqual(fullname.fullname('First', 'Last'), 'First Last')

    def test_formattedname(self):
        self.assertEqual(fullname.fullname('first', 'last'), 'First Last')

    def test_emptyname(self):
        self.assertRaises(ValueError)

if __name__ == "__main__":
    unittest.main(verbosity=2)