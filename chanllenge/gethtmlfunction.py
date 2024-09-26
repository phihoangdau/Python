import re
import urllib.request
def gethtmlcontent (string1, index):
    html = urllib.request.urlopen(string1).read().decode()
    data = re.findall("<!--(.*?)-->", html, re.DOTALL)[index]
    return data