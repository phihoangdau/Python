import urllib.request
import re
import string

nl = []
list_apha = list(string.ascii_lowercase)
html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read().decode()
data = list(re.findall("<!--(.*?)-->", html, re.DOTALL)[-1])
for i in data:
    if i not in list_apha:
        pass
    else:
        nl.append(i)
print("".join(nl))
