import urllib2
from bs4 import BeautifulSoup
from multiprocessing import Pool


def crawl():
    applist = open('absent_google_play').readlines()
    apptag  = open('app_tag.wandoujia.csv', 'w')
    apptag.close()
    # multi-tasks
    n = 4
    p = Pool(n)
    for i in range(n):
        p.apply_async(subtask, args=(applist[:20], n, i))
    p.close()
    p.join()


def subtask(applist, n, i):
    # query every n app starting from i-th app
    for app in applist[i::n]:
        app = app.strip()
        url = 'http://www.wandoujia.com/apps/%s' % app
        try:
            page = urllib2.urlopen(url, timeout=5).read()
            soup = BeautifulSoup(page)
            tags = soup(class_='tag-box')[0].text.encode('u8').strip().replace('\n', '_')
            apptag = open('app_tag.wandoujia.csv', 'a')
            print >> apptag, app + ',' + tags
            apptag.close()
        except:
            apptag = open('app_tag.wandoujia.csv', 'a')
            print >> apptag, app + ',' + 'except'
            apptag.close()
            

if __name__ == '__main__':
    crawl()
