def pat1(n):
    for i in range(1,n+1):
        for j in range(0,i):
            print(i,end=' ')
        print('\r')
n=int(input())
pat1(n)
