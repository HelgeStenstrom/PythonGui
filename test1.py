import tkinter as tk
#print("test1.py imported")

class HelloApp(tk.Frame):
    # Based on https://docs.python.org/3.4/library/tkinter.html
    def __init__(self, master = None):
        self.master = master
        tk.Frame.__init__(self, self.master)
        self.pack()
        self.createWidgets()

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
        #help(self.mainloop)
        self.mainloop()


def main():
    # Interactive run only.
    root = tk.Tk()
    app = HelloApp(root)
    app.mainloop()

if __name__ == '__main__':
    main()

