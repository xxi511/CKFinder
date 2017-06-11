from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from urllib.request import Request
import threading


class CKCrawler(object):
    def __init__(self, tid, keywod, p1, p2):
        homeData = self.getpageData(tid, 1)
        lastPage = int(homeData.find('a', class_="last").string[3:])
        p2 = lastPage if p2 == 99999 else p2
        self.err = None
        if p1 > lastPage or p2 > lastPage:
            self.err = '好像沒這麼多頁喔'
            return

        self.donelist = []
        self.findlist = {}
        self.total = p2 - p1 + 1
        self.th1, self.th2, self.th3 = self.createThread(p1, p2, tid, keywod)

    def getpageData(self, tid, page):
        url = 'https://ck101.com/thread-{}-{}-1.html'.format(tid, page)
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'})
        data = bs(urlopen(req).read(), 'lxml')
        return data

    def createThread(self, p1, p2, tid, keyword):
        total = p2 - p1 + 1

        def search(start, end):
            for i in range(start, end):
                data = self.getpageData(tid, i)
                articles = data.find_all('td', class_="t_f")
                for article in articles:
                    pid = article.attrs['id'].split('_')[-1]
                    content = article.text.replace('\r\n', '')
                    idx = content.find(keyword)
                    if idx == -1:
                        continue
                    num = 100
                    grabs = max(idx - num, 0)
                    grage = idx + len(keyword) + num
                    self.findlist[pid] = content[grabs:grage]
                self.donelist.append(i)

        if total <= 3:
            th1 = threading.Thread(target=search, args=(p1, p2 + 1))
            th2 = threading.Thread(target=search, args=(p1, p1))
            th3 = threading.Thread(target=search, args=(p1, p1))
        else:
            gap = self.total // 3
            s1, s2, s3, s4 = p1, p1 + gap, p1 + 2 * gap, p2 + 1
            th1 = threading.Thread(target=search, args=(s1, s2))
            th2 = threading.Thread(target=search, args=(s2, s3))
            th3 = threading.Thread(target=search, args=(s3, s4))

        return th1, th2, th3

    def startThread(self):
        self.th1.start()
        self.th2.start()
        self.th3.start()
