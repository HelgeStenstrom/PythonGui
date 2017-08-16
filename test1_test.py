import unittest
import test1
import tkinter as tk


# Based on idea in https://stackoverflow.com/questions/4083796/how-do-i-run-unittest-on-a-tkinter-app

class FakeApp(test1.HelloApp):
    def mainloop(self):
        print("FakeApp.mainloop called")

def fakeMainloop():
    print("fakeMainLoop called")

def fakeMainLoop_self(self):
    # TODO: Förstå varför self-argumentet inte fungerar. Jämför med web-exempel
    print("fakeMainLoop_self called")

class TkAppTests(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()

    def tearDown(self):
        try:
            self.root.destroy()
        except tk._tkinter.TclError:
            # This is what happens if the destroy function is already called on the root object.
            pass

    def test_mainloop_with_GUi(self):
        # TODO: Förstå varför detta test gör att många GUI öppnas. Testen är inte oberoende!
        app = test1.HelloApp(self.root)
        app.start()

    def test_fake_mainloop_by_subclassing(self):
        app = FakeApp(self.root)
        app.mainloop()

    def test_fake_mainloop_by_replaced_method(self):
        app = test1.HelloApp(self.root)
        app.mainloop = fakeMainloop
        app.mainloop()

    def test_changing_start_of_app(self):
        app = test1.HelloApp(self.root)
        app.mainloop = fakeMainloop
        app.start()

    def test_patch_with_self(self):
        app = test1.HelloApp(self.root)
        app.mainloop = fakeMainLoop_self
        app.start()

    def test_detecting_mainloop_call(self):
        app = test1.HelloApp(self.root)
        def fakeMainLoop():
            self.called = True
            print("inner fake called")
        app.mainloop = fakeMainLoop
        app.start()
        self.assertTrue(self.called)


if __name__ == '__main__':
    unittest.main()
