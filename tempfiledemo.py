# Python 3

import tempfile
import unittest


class ClassToBeTested:
    def __init__(self, f):
        self.file = f
        
    def function_to_be_tested(self):
        fd = open(self.file, "rb")
        print("open and read: ", self.file)
        contents = fd.read()
        fd.close()
        return contents


# Unit testing
class SomeTests(unittest.TestCase):
    def setUp(self):
        self.thefile = tempfile.NamedTemporaryFile()
        print("create: ", self.thefile.name)
        self.c = ClassToBeTested(self.thefile.name)

    def tearDown(self):
        print("closing ", self.thefile.name)
        self.thefile.close()

    def test_that_file_is_read(self):
        # setup
        self.thefile.write(b"abc")
        self.thefile.flush()

        # exercise
        result = self.c.function_to_be_tested()
        # On windows, this gives a ResourceWarning, because the file
        # is opened for read, but not closed. The file is closed
        # later, by tearDown.

        print("self.thefile: ", self.thefile)
        self.thefile.close()

        # verify
        self.assertEqual(result, b"abc")


if __name__ == "__main__":
    unittest.main()
