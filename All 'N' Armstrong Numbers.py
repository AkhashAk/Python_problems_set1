def is_armstrong_num(n):
    s=0
    t=n
    while(n>0):
        r=n%10
        s=s+r**3
        n=n//10
    if t==s:
        return True
def all_armnum(n):
    t=n
    for i in range(1,n+1):
        a=is_armstrong_num(i)
        if a==True:
            print(i)
n=int(input())
all_armnum(n)
