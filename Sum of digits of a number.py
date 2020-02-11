def sum_dig(l):
    s=0
    for i in range(len(l)):
        s=s+l[i]
    return print(s)
l=list(map(int,input()))
sum_dig(l)
