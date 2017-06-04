from tkinter import messagebox, Tk, W, E
from tkinter.ttk import Label, Button, Entry, Progressbar, Frame

class FinderUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.grid()
        self.parent = parent

        self.urlHint = Label(self, text='請輸入網址:', width=10, padding=3)
        self.urlHint.grid(row=0, column=0, columnspan=2)
        self.urlEntry = Entry(self, width=40)
        self.urlEntry.grid(row=0, column=2, columnspan=8)

        self.keyHint = Label(self, text='尋找內容:', width=10, padding=3)
        self.keyHint.grid(row=1, column=0, columnspan=2)
        self.keyEntry = Entry(self, width=40)
        self.keyEntry.grid(row=1, column=2, columnspan=8)

        self.pageHint = Label(self, text='尋找範圍:', width=10, padding=3)
        self.pageHint.grid(row=2, column=0, columnspan=2)
        self.p1Entry = Entry(self, width=5)
        self.p1Entry.grid(row=2, column=2, stick=W)
        self.rangeHint = Label(self, text='~')
        self.rangeHint.grid(row=2, column=3, stick=W)
        self.p2Entry = Entry(self, width=5)
        self.p2Entry.grid(row=2, column=4, stick=W)
        self.p2Hint = Label(self, text='(留空代表最後一頁)')
        self.p2Hint.grid(row=2, column=5, stick=W)

        self.bar = Progressbar(self, orient="horizontal",
                               length=220, mode="determinate")
        self.bar.grid(row=3, column=0, columnspan=5)
        self.btn = Button(self, text='搜尋')
        self.btn.grid(row=3, column=5, columnspan=5, stick=E)


if __name__ == '__main__':
    root = Tk()
    root.resizable(0, 0)
    root.geometry("380x110")
    app = FinderUI(root)
    root.mainloop()