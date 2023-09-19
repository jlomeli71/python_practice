import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
# url = 'http://py4e-data.dr-chuck.net/comments_42.json'

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
# print(data.decode())

info = json.loads(data)
# print(len(info['comments']))
# print(type(info['comments']))
count = 0
total = 0
for each in info['comments']:
    count += 1
    total += each['count']
print("Count:", count)
print("Sum:", total)


'''for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
'''
# Sample data: 
# http://py4e-data.dr-chuck.net/comments_42.json
# Sum=2553

# Actual data: 
# http://py4e-data.dr-chuck.net/comments_1811788.json 
# Sum ends with 73

# Json example
'''
{
  comments: [
    {
      name: "Matthias"
      count: 97
    },
    {
      name: "Geomer"
      count: 97
    }
    ...
  ]
}
'''

# Output example
'''
$ python3 solution.py
Enter location: http://py4e-data.dr-chuck.net/comments_42.json
Retrieving http://py4e-data.dr-chuck.net/comments_42.json
Retrieved 2733 characters
Count: 50
Sum: 2...
'''


'''

data = """
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]"""

info = json.loads(data)
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])

'''