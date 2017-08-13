import unittest
import test1
import tkinter as tk


# Based on idea in https://stackoverflow.com/questions/4083796/how-do-i-run-unittest-on-a-tkinter-app

class FakeTk(tk.Tk):
    def mainloop(self):
        print("FakeTk.mainloop called,")
        pass

class TkAppTests(unittest.TestCase):
    def test_that_App_can_be_created(self):
        print("dict Tk 1 = ", tk.__dict__['Tk'])
        # tk.__dict__['Tk'] = FakeTk
        print("dict Tk 2 = ", tk.__dict__['Tk'])
        print("tk.Tk = ", tk.Tk)
        r = tk.Tk()
        # print("r = ", r)
        a = test1.App(r)
        self.assertIsNotNone(a.mainloop)
        a.mainloop()

if __name__ == '__main__':
    unittest.main()
