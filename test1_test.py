import unittest
import test1
import tkinter as tk


# Based on idea in https://stackoverflow.com/questions/4083796/how-do-i-run-unittest-on-a-tkinter-app

def fakeMainloop(self):
    pass


class FakeHelloApp(test1.HelloApp):
    def mainloop(self):
        pass

@unittest.skip
class HelloAppTests(unittest.TestCase):

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
        app = FakeHelloApp(self.root)
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


class ButtonsAppTests(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = test1.ButtonApp(self.root)

    def test_that_app_can_be_started(self):
        self.app.start()

    def test_that_click_list_is_initially_empty(self):
        self.assertEqual(self.app.clicks, [])

    def test_that_calling_click_detector_adds_to_click_list(self):
        self.app.clickDetector("one")
        self.app.clickDetector("two")
        self.assertEqual(self.app.clicks, ["one", "two"])


    def test_manually_that_Quit_quits(self):

        self.assertFalse(self.app.started)
        self.assertFalse(self.app.stopped)

        self.app.start()

        self.assertTrue(self.app.started)
        self.assertTrue(self.app.stopped)

    def Qtest_manually_that_button_is_clicked(self):
        print("Click buttons in order, end with Quit")

        pass

if __name__ == '__main__':
    unittest.main()
