import threading
import urllib2
import time
import lxml.html
import xml.dom.minidom
from socket import timeout

outfile3 = open("easy_sites.txt","w+")
workday_links = []
a = ["workday", "jobvite", "workable", "smartrecruiters", "greenhouse", "lever.co/"]

start = time.time()
with open('areers.txt') as result:
    urls = result.read().splitlines()

def fetch_url(url):
    try:
        urlHandler = urllib2.urlopen(url, timeout=2)
        # print "'%s\' fetched in %ss" % (url, (time.time() - start))
        dom =  lxml.html.fromstring(urlHandler.read())
        for link in dom.xpath('//a/@href'): # select the url in href for all a tags(links)
            if any(x in link for x in a):
                print link
                workday_links.append(link)
                return
    except Exception as err:
        j = 'bala'

threads = [threading.Thread(target=fetch_url, args=(url,)) for url in urls]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

outfile3.write("\n".join(set(workday_links)))
outfile3.close()
print "Elapsed Time: %s" % (time.time() - start)
