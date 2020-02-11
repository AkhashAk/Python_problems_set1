def perfect_num(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s=s+i
    return s
n=int(input())
m=perfect_num(n)
if m==n:
    print(n,'is a perfect number')
else:
    print(n,'is not a perfect number')
