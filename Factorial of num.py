def fac(n):
    s=1
    while n>0:
        s=s*n
        n-=1
    return s
n=int(input())
print(fac(n))
