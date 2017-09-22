# ============== Unit tests =================================
import unittest
import finddups as d

class ExampleTests(unittest.TestCase):
    'tests various aspects of the Example class'
    def setUp(self):
        print "another test"
        pass
    def testSomething(self):
        'A test that should be successful'
        return 17


if __name__ == '__main__':
    unittest.main()
