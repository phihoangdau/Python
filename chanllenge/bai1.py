import string
from bai2function import alphabet
s = input()
ns = []
list_aphalbet = list(string.ascii_lowercase)

for i in s:
    if i not in list_aphalbet:
        ns.append(i)
    else:
        ni = list_aphalbet.index(i)+2
        if ni >= len(list_aphalbet):
            ni -= len(list_aphalbet)
            ns.append(list_aphalbet[ni])
        else:
            ns.append(list_aphalbet[ni])
print("".join(ns))
print(alphabet("de ghi", 4))
print(list_aphalbet)

        
        
        

       
    
