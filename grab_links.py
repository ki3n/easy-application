import urllib
import lxml.html
import xml.dom.minidom
f= open("guru99.txt","w+")
with open('/Users/kiran/CodeVS/ohryro/grab_careers/data.txt') as result:
    lines = result.read().splitlines()
# print lines
careers_array = []
not_found_array = []
for i in range(len(lines)):
    print "----------------------------"
    print lines[i]
    try:
        connection = urllib.urlopen(lines[i])
        dom =  lxml.html.fromstring(connection.read())
        for link in dom.xpath('//a/@href'): # select the url in href for all a tags(links)
            if 'careers' in link:
                if link.startswith( '/' ) or link.startswith( 'careers' ):
                    print lines[i]+link
                    careers_array.append(lines[i]+link)
                    f.write(lines[i]+link)
                    f.write("\r\n")
                else:
                    print link
                    careers_array.append(link)
                    f.write(link)
                    f.write("\r\n")
            elif 'jobs' in link:
                if link.startswith( '/' ) or link.startswith( 'jobs' ):
                    print lines[i]+link
                    careers_array.append(lines[i]+link)
                    f.write(lines[i]+link)
                    f.write("\r\n")
                else:
                    print link
                    careers_array.append(link)
                    f.write(link)
                    f.write("\r\n")
            else:
                not_found_array.append(lines[i])
    except Exception as err:
        print err

print set(not_found_array)
print set(careers_array)