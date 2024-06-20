import unittest
from src import serviceArea

class TestServiceArea(unittest.TestCase):

    # basic
    def setUp(self):
        self.bigSquare = serviceArea(3, 0)
    
    def tearDown(self):
        del self.bigSquare

    def test_arrival_rate(self):
        self.assertEqual(self.bigSquare.computeArrivalRate(), 3/10)
    
    def test_mean(self):
        self.assertEqual(self.bigSquare.computeMean(), 3) 

    def test_variance(self):
        self.assertEqual(self.bigSquare.computeVariance(), 21/2) 

    def test_response_time(self):
        self.assertEqual(self.bigSquare.computeResponseTime(), 18.749999999999986) 

class TestServiceAreaSmall(unittest.TestCase):
    
    # basic
    def setUp(self):
        self.smallSquare = serviceArea(2, 0)
    
    def tearDown(self):
        del self.smallSquare

    def test_arrival_rate(self):
        self.assertEqual(self.smallSquare.computeArrivalRate(), 2/15)
    
    def test_mean(self):
        self.assertEqual(self.smallSquare.computeMean(), 2) 

    def test_variance(self):
        self.assertEqual(self.smallSquare.computeVariance(), 14/3)

class TestServiceAreaWithHole(unittest.TestCase):

    def setUp(self):
        # D2 only
        self.squareWithHole = serviceArea(3, 2)
    
    def tearDown(self):
        del self.squareWithHole

    def test_arrival_rate(self):
        self.assertEqual(self.squareWithHole.computeArrivalRate(), 1/6)
    
    def test_mean(self):
        self.assertEqual(self.squareWithHole.computeMean(), 19/5) 

    def test_variance(self):
        self.assertEqual(self.squareWithHole.computeVariance(), 91/6) 

if __name__ == "__main__":
    unittest.main()