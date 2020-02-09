from BinaryTreeHeight import getHeightFor
import unittest

class BinaryTreeHeightTest(unittest.TestCase):

    def test_singleNodeTreeHeightIsCero(self):
        self.assertTrue(getHeightFor('1', '8') == 0)

    def test_TwoLevelsTreeHeightIsOne(self):
        self.assertTrue(getHeightFor('3', '3 2 5') == 1)

    def test_FourLevelsTreeHeightIsThree(self):
        self.assertTrue(getHeightFor('7', '3 2 5 1 4 6 7'))


if __name__ == '__main__':
    unittest.main()