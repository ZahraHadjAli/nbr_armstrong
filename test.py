import unittest
import armstrg


class Test(unittest.TestCase):
    """
    Tests pour les fonctions de armstrg
    """

    def test_valid0(self):
        self.armstrg(armstrg.armstrg(0), 1)

    def test_valid1(self):
        self.armstrg(armstrg.armstrg("1"), 1)

    def test_valid153(self):
        self.armstrg(armstrg.armstrg("153"), 1)

    def test_valid371(self):
        self.armstrg(armstrg.armstrg("371"), 1)

    def test_valid407(self):
        self.armstrg(armstrg.armstrg("407"), 1)

    def test_valid555(self):
        self.armstrg(armstrg.armstrg("555"), 0)

    def test_valid6(self):
        self.armstrg(armstrg.armstrg("6"), 0)

    def test_valid905(self):
        self.armstrg(armstrg.armstrg("905"), 0)


    if __name__ == "__main__":
        unittest.main()
