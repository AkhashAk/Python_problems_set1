def rev_num(n):
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    return print(s)
n=int(input())
rev_num(n)
