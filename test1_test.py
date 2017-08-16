import unittest
import test1
import tkinter as tk


# Based on idea in https://stackoverflow.com/questions/4083796/how-do-i-run-unittest-on-a-tkinter-app

def fakeMainloop(self):
    pass


class FakeApp(test1.HelloApp):
    def mainloop(self):
        pass


class TkAppTests(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.savedMainLoop = self.root.mainloop

    def tearDown(self):
        self.root.mainloop = self.savedMainLoop
        try:
            self.root.destroy()
        except tk._tkinter.TclError:
            # This is what happens if the destroy function is already called on the root object.
            pass

    @unittest.skip
    def test_mainloop_with_GUi(self):
        app = test1.HelloApp(self.root)
        print("is this ignored?")
        app.start()

    def test_fake_mainloop_by_subclassing(self):
        app = FakeApp(self.root)
        app.mainloop()

    def test_fake_mainloop_by_replaced_method(self):
        app = test1.HelloApp(self.root)
        app.mainloop = fakeMainloop
        app.mainloop(app)

    def test_changing_start_of_app(self):
        app = test1.HelloApp(self.root)
        app.mainloop = fakeMainloop
        app.start()

    def test_detecting_mainloop_call(self):
        app = test1.HelloApp(self.root)
        app.called = False

        def fakeMainLoop(other):
            other.called = True

        app.mainloop = fakeMainLoop

        app.start()

        self.assertTrue(app.called)


if __name__ == '__main__':
    unittest.main()
