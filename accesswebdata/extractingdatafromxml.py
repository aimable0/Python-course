from urllib import request
import xml.etree.ElementTree as ET

# url = input('Enter url: ')
url = "http://py4e-data.dr-chuck.net/comments_2052982.xml"
data = request.urlopen(url).read()
string_data = data.decode()

# check..1
print(type(string_data))


# working with xml

tree = ET.fromstring(string_data) # this is giving me a root
# check one two...
# print(type(tree))
# counts  = tree.findall('comments/comment/count')

# print(type(counts))

# sum = 0
# for item in counts:
#     num = int(item.text)
#     sum += num
# print(sum)

counts = tree.findall(".//count")
print(type(counts))
print(counts)

sum = 0
for item in counts:
    num = int(item.text)
    sum += num
print(sum)