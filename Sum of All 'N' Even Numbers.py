def sum_even(n):
    s=0
    t=n
    for i in range(1,n+1):
        if t%2!=0:
            s=s+i
        t-=1
    return print(s)
n=int(input())
sum_even(n)
