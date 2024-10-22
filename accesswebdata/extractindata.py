import json
from urllib import request
from rich import print_json
url = "http://py4e-data.dr-chuck.net/comments_2052983.json"

response = request.urlopen(url).read()
parsed_json = json.loads(response)
print(type(parsed_json))

i = 0
sum = 0
for n in parsed_json['comments']:
    num = int(parsed_json['comments'][i]['count'])
    sum += num
    i += 1
print(sum)
# for line in parsed_json['comments'][0]

