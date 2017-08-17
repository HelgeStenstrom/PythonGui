import tkinter as tk
#print("test1.py imported")


class ButtonWithArgument():
    pass

class BasicApp(tk.Frame):
    def __init__(self, master = None):
        self.master = master
        tk.Frame.__init__(self, self.master)
        self.pack()
        self.createWidgets()



class HelloApp(BasicApp):
    # Based on https://docs.python.org/3.4/library/tkinter.html
    def createWidgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.QUIT = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.QUIT.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

    def start(self):
        self.mainloop(self)




class ButtonApp(BasicApp):
    def __init__(self, master = None):
        super().__init__(master)
        self.clicks = []
        self.started = False
        self.stopped = False

    def createWidgets(self):
        # self.hi_there = tk.Button(self)
        # self.hi_there["text"] = "Hello World\n(click me)"
        # self.hi_there["command"] = self.say_hi
        # self.hi_there.pack(side="top")

        self.QUIT = tk.Button(self, text="QUIT", fg="red",
                              command=self.stop)
        self.QUIT.pack(side="bottom")
        pass

    def clickDetector(self, argument):
        self.clicks += [argument]

    def start(self):
        self.started = True
        self.mainloop()

    def stop(self):
        self.stopped = True
        self.master.destroy()


def main():
    # Interactive run only.
    root = tk.Tk()
    app = HelloApp(root)
    app.mainloop()

if __name__ == '__main__':
    main()

