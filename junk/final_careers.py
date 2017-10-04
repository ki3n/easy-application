import threading
import urllib2
import time
import lxml.html
import xml.dom.minidom
from socket import timeout

outfile3 = open("final.txt","w+")

with open('/Users/kiran/CodeVS/ohryro/grab_careers/careers.txt') as result:
    urls = result.read().splitlines()

outfile3.write("\n".join(set(urls)))
outfile3.close()