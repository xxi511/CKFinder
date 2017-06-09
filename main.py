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
        self.btn = Button(self, text='搜尋', command=self.clickBtn)
        self.btn.grid(row=3, column=5, columnspan=5, stick=E)

    def clickBtn(self):
        url = self.checkurl()
        if url is None:
            messagebox.showerror('網址錯誤', '這是卡提諾的網址嗎')
            return

        keyword = self.keyEntry.get().strip()
        if keyword == '':
            messagebox.showerror('關鍵字錯誤', '關鍵字是空的')
            return

        pageErr, p1, p2 = self.checkpage()
        if pageErr:
            messagebox.showerror('頁數錯誤', '請輸入大於0的整數')
            return


    def checkurl(self):
        # https://ck101.com/thread-3885080-1-1.html
        # https://ck101.com/forum.php?mod=viewthread&tid=3434923&page=13
        # https://ck101.com/forum.php?mod=viewthread&tid=3434923&page=13&extra=#pid99055328
        urlStr = self.urlEntry.get()
        if urlStr.startswith('https://ck101.com/thread'):
            tid = urlStr.split('-')[1]
        elif urlStr.startswith('https://ck101.com/forum.php?'):
            tid = urlStr.split('&')[1][4:]
        else:
            tid = None

        return 'https://ck101.com/thread-{}-1-1.html'.format(tid) if tid else None

    def checkpage(self):
        p1str = self.p1Entry.get()
        p2str = self.p2Entry.get()
        p1 = int(p1str) if p1str.isdigit() else None
        p2 = int(p2str) if p2str.isdigit() else 99999

        if p1 is None:
            return 'err', None, None

        p1, p2 = max(0, p1), max(0, p2)
        if p1 == 0 or p2 == 0:
            return 'err', None, None

        return None, p1, p2

if __name__ == '__main__':
    root = Tk()
    root.resizable(0, 0)
    root.geometry("380x110")
    app = FinderUI(root)
    root.mainloop()