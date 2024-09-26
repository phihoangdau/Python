if __name__ == '__main__':
    a = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        # add item into a list
        a.append([name, score])
    # sort for name alphabet
    a.sort()
    # remove all the lowest score 
    b = [i for i in a if i[0] != a[0][0]]
    c = [j for j in b if j[0] == b[0][0]]

    c.sort(key=lambda x : x[1])
    for i in range(len(c)):
        print(c[i][1])