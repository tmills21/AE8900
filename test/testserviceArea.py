import unittest
from src import serviceAreaSquare, StandardResponseArea, PriorityResponseArea

class TestServiceArea(unittest.TestCase):

    # basic
    def setUp(self):
        self.bigSquare = StandardResponseArea(3, 0)
    
    def tearDown(self):
        del self.bigSquare

    def test_arrival_rate(self):
        self.assertEqual(self.bigSquare.computeArrivalRate(), 3/10)
    
    def test_mean(self):
        self.assertEqual(self.bigSquare.computeExpectation(), 3) 

    def test_variance(self):
        self.assertEqual(self.bigSquare.computeExpectationVarSq(), 21/2) 

    def test_response_time(self):
        self.assertAlmostEqual(self.bigSquare.computeResponseTime(), 18.75) 

class TestServiceAreaSmall(unittest.TestCase):

    # D1 only
    def setUp(self):
        self.smallSquare = serviceAreaSquare(2, 0)
    
    def tearDown(self):
        del self.smallSquare

    def test_arrival_rate(self):
        self.assertEqual(self.smallSquare.computeArrivalRate(), 2/15)
    
    def test_mean(self):
        self.assertEqual(self.smallSquare.computeExpectation(), 2) 

    def test_variance(self):
        self.assertEqual(self.smallSquare.computeExpectationVarSq(), 14/3)

class TestServiceAreaWithHole(unittest.TestCase):

    # D2 only
    def setUp(self):
        self.squareWithHole = serviceAreaSquare(3, 2)
    
    def tearDown(self):
        del self.squareWithHole

    def test_arrival_rate(self):
        self.assertEqual(self.squareWithHole.computeArrivalRate(), 1/6)
    
    def test_mean(self):
        self.assertEqual(self.squareWithHole.computeExpectation(), 19/5) 

    def test_variance(self):
        self.assertEqual(self.squareWithHole.computeExpectationVarSq(), 91/6) 

class TestResponseWithHole(unittest.TestCase):

    # D2 only
    def setUp(self):
        self.squareWithHole = PriorityResponseArea(3, 2)
    
    def tearDown(self):
        del self.squareWithHole

    def test_arrival_rate(self):
        self.assertEqual(self.squareWithHole.computeArrivalRate(), 1/6)
    
    def test_mean(self):
        self.assertEqual(self.squareWithHole.computeExpectation(), 19/5) 

    def test_variance(self):
        self.assertEqual(self.squareWithHole.computeExpectationVarSq(), 91/6) 

    def test_responseTime(self):
        self.assertAlmostEqual(self.squareWithHole.computeResponseTime(), 15.89, 2) 

if __name__ == "__main__":
    unittest.main()