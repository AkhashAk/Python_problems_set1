def pow(n,k):
    m=n
    for i in range(k-1):
        n=n*m
    return print(n)
n,k=map(int,input().split())
pow(n,k)
