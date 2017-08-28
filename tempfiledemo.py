# Python 3

import tempfile
import unittest

class ClassToBeTested:
    def __init__(self, f):
        self.file = f
        
    def functionToBeTested(self):
        fd = open(self.file, "rb")
        
        return fd.read()

# Unit testing

class SomeTests(unittest.TestCase):
    def setUp(self):
        self.thefile = tempfile.NamedTemporaryFile()
        self.c = ClassToBeTested(self.thefile.name)

    def tearDown(self):
        self.thefile.close()

    # def test_that_fails(self):
    #     self.fail()

    def test_that_file_is_read(self):
        # setup
        self.thefile.write(b"abc")
        self.thefile.flush()
        
        result = self.c.functionToBeTested()
        self.assertEqual(result, b"abc")
        pass

    


if __name__ == "__main__":
    unittest.main()

    
