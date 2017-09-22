import unittest

import finddups


class FunctionTests(unittest.TestCase):
    """tests various aspects of the Example class"""

    def testSomething(self):
        """A test that should be successful"""
        pass

    def testF(self):
        startDir = "."

        expected = ["x"]
        actual = finddups.getFileList(startDir)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
