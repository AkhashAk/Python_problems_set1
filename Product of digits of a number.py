def product_ofdigits(l):
    s=1
    for i in range(len(l)):
        s=s*l[i]
    return print(s)
l=list(map(int,input()))
product_ofdigits(l)
