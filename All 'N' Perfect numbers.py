def isperfect_num(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s=s+i
    if s==n:
        return True
def perfect_num(n):
    for i in range(1,n+1):
        p=isperfect_num(i)
        if p==True:
            print(i)
n=int(input())
perfect_num(n)
