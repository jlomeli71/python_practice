import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# url = 'http://py4e-data.dr-chuck.net/comments_42.xml' # This url sum is 2553
# url = 'http://py4e-data.dr-chuck.net/comments_1811787.xml' # This url sum ens with 52

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
# print(data.decode())
tree = ET.fromstring(data)

comments = tree.findall('comments/comment')

count = 0
total = 0

for coment in comments:
    count += 1
    total += int(coment.find('count').text)
    # print('Count', coment.find('count').text)

print('Count:', count)
print('Sum:', total)


