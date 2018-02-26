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

    def test_that_files_are_in_dict(self):
        """Store files in a dict"""
        # Setup
        startDir = "exampleFiles"

        # Exercise
        aDict = finddups.getFileDict(startDir)

        # Verify
        self.assertIn(["exampleFiles/adir/a.txt"], aDict.values(), "find a file that is in the folder")



class Md5Tests(unittest.TestCase):
    def test_my_md5(self):
        fn = "warehouse.py"
        result = finddups.myMd5(fn)
        self.assertEqual("f4ed7887b2a7a50cdc7b0b1c59b096f1",result)

if __name__ == '__main__':
    unittest.main()
