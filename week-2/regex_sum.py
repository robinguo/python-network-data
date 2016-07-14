import re

handle = open("regex_sum_297371.txt")
content = handle.read()
numbers = re.findall('[0-9]+', content)
# print numbers
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
# print numbers
print sum(numbers)
