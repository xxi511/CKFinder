from tkinter import messagebox, Tk
from tkinter.ttk import Label, Button, Entry, Progressbar, Frame

class FinderUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.grid()
        self.parent = parent

        self.urlHint = Label(self, text='請輸入網址:', width=10, padding=3)
        self.urlHint.grid(row=0, column=0, columnspan=2)
        self.urlEntry = Entry(self, width=50)
        self.urlEntry.grid(row=0, column=2, columnspan=10)

        self.keyHint = Label(self, text='尋找內容:', width=10, padding=3)
        self.keyHint.grid(row=1, column=0, columnspan=2)
        self.keyEntry = Entry(self, width=50)
        self.keyEntry.grid(row=1, column=2, columnspan=10)

        self.pageHint = Label(self, text='尋找範圍:', width=10, padding=3)
        self.pageHint.grid(row=2, column=0, columnspan=2)
        self.p1Entry = Entry(self, width=5)
        self.p1Entry.grid(row=2, column=2)
        self.rangeHint = Label(self, text='~', width=5)
        self.rangeHint.grid(row=2, column=3)
        self.p2Entry = Entry(self, width=5)
        self.p2Entry.grid(row=2, column=4)


if __name__ == '__main__':
    root = Tk()
    root.resizable(0, 0)
    root.geometry("450x200")
    app = FinderUI(root)
    root.mainloop()