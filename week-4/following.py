import urllib
from BeautifulSoup import *

url = raw_input("Enter URL: ")
count = raw_input("Enter count: ")
count = int(count)
position = raw_input("Enter position: ")
position = int(position)

while count >= 0:
    print "Retrieving:", url
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup("a")
    url = tags[position - 1].get("href", None)
    count -= 1
