import json
import urllib

url = raw_input("Enter location: ")
print "Retrieving", url
data =  urllib.urlopen(url).read()
print "Retrieved", len(data), " characters"
comments = json.loads(data).get("comments")
sum = 0
count = 0
for comment in comments:
    sum += comment.get("count")
    count += 1
print "Count", count
print "Sum", sum
