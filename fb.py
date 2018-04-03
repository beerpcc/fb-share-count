import urllib2, json, time
from random import randint
import sys

fname = 'urls.txt'
with open(fname) as f:
    lines = f.readlines()

# Strip newline
lines = [x.strip() for x in lines]

urls_array = []
tmp_array = []
for i in range(len(lines)):
    if(i % 50 == 0):
        if len(tmp_array) > 0:
            urls_array.append(tmp_array)
        tmp_array = []
        tmp_array.append(lines[i])
    else:
        tmp_array.append(lines[i])
        if(i >= len(lines)-1):
            urls_array.append(tmp_array)

# loop through lines
for urlset in urls_array:
    urls = ""
    tmp_urls_array = []
    for line in urlset:
        urls += line + ","
        tmp_urls_array.append(line)
    request = urllib2.Request("https://graph.facebook.com/?ids=" + urls[:-1])
    response = urllib2.urlopen(request)
    data = json.loads(response.read())
    for i in range(len(tmp_urls_array)):
        print data[tmp_urls_array[i]]["share"]["share_count"]
        with open("result.txt", "a") as f:
            f.write(str(data[tmp_urls_array[i]]["share"]["share_count"]) + '\n')
    time.sleep(25)