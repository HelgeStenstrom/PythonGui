import unittest

import finddups


def filterFileList(aList):
    filteredList = [n for n in aList if "DS" not in n]
    return filteredList


class UtilityTests(unittest.TestCase):

    def test_that_DS_are_removed(self):
        l = ['a', 'xDSx', 'b']
        self.assertEqual(['a', 'b'], filterFileList(l))


class FunctionTests(unittest.TestCase):
    """tests various aspects of the Example class"""

    def testSomething(self):
        """A test that should be successful"""
        pass

    def test_that_files_are_found(self):
        # Setup
        startDir = "exampleFiles"

        # Exercise
        aList = finddups.getFileList(startDir)

        # Post process for beter determinism
        filteredList = filterFileList(aList)

        # Verify
        self.assertIn("exampleFiles/adir/a.txt", filteredList, "find a file that is in the folder")
        self.assertEqual(4, len(filteredList), "Number of files in example folder")


if __name__ == '__main__':
    unittest.main()
