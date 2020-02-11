def armstrong_num(n):
    s=0
    while(n>0):
        r=n%10
        s=s+r**3
        n=n//10
    return s
n=int(input())
m=armstrong_num(n)
if n==m:
    print('It is armstrong number')
else:
    print("it is not armstrong number")
