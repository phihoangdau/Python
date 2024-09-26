from operator import truediv
import re
import urllib.request

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
#number = "12345"
number = str(16044/2)
# this is create a new partten and we will look only in this 
pattern = re.compile("and the next nothing is (\d+)")
while True:
    content = urllib.request.urlopen(url % number).read().decode()
    print(content)
    ns = pattern.search(content)
    if ns == None:
        break
    else:
        number = ns.group(1)



