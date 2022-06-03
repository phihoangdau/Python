import requests
import string

url = input()
nl = []
# get content of the html source code
x = requests.get(url)

# print the response (the content of the request file)
list1 = list(x.text)

list_apha = list(string.ascii_lowercase)
for i in list1:
    if i not in list_apha:
        pass
    else:
        nl.append(i)
print("".join(nl))