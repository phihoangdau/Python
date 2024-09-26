import urllib.request
import re
import string

nl = []
list_apha = list(string.ascii_lowercase)
# the decode() in here to convert the html type to string 
html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read().decode()
#
data = list(re.findall("<!--(.*?)-->", html, re.DOTALL)[-1])
for i in data:
    if i not in list_apha:
        pass
    else:
        nl.append(i)
print("".join(nl))
