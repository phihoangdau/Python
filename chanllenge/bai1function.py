import string
def alphabet(newstring, step):
    list_alphabe = list(string.ascii_lowercase)
    ns = []
    for i in newstring:
        if i not in list_alphabe:
            ns.append(i)
        else:
            ni = list_alphabe.index(i)+step
            if ni >= len(list_alphabe):
                ni -= len(list_alphabe)
                ns.append(list_alphabe[ni])
            else:
                ns.append(list_alphabe[ni])  
    return("".join(ns))

print(alphabet("ab [] def", 3))
