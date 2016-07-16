import urllib
import xml.etree.ElementTree as ET

url = raw_input("Enter location: ")
print "Retrieving ", url
xml = urllib.urlopen(url).read()
print 'Retrieved',len(xml),'characters'
tree = ET.fromstring(xml)

count = 0
sum = 0
comments = tree.findall(".//comment")
for comment in comments:
    count += 1
    sum += int(comment.find("count").text)
print "Count: ", count
print "Sum: ", sum
