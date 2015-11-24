import urllib2
import re
from multiprocessing import Pool


def crawl():
    applist = open('app_list_for_crawl').readlines()
    apptag  = open('app_tag.csv', 'w')
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
        url = 'https://play.google.com/store/apps/details?id=%s' % app
        try:
            page = urllib2.urlopen(url, timeout=5).read()
            m = re.search(r'<span itemprop=\"genre\">(.*?)</span>', page)
            apptag = open('app_tag.csv', 'a')
            print >> apptag, app + ',' + m.group(1)
            apptag.close()
        except:
            apptag = open('app_tag.csv', 'a')
            print >> apptag, app + ',' + 'except'
            apptag.close()
            

if __name__ == '__main__':
    crawl()
