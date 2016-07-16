import urllib
from BeautifulSoup import *

url = raw_input("Enter - ")
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

count = 0
sum = 0
tags = soup("span")
for tag in tags:
    sum += int(tag.contents[0])
    count += 1

print "Count", count
print "Sum", sum
