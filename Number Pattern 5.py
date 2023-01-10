def pat5(n):
    k=2*n-n
    for i in range(1,n+1):
        for j in range(0,k):
            print(' ',end='')
        k=k-1
        for j in range(0,i):
            print(i,end=' ')
        print('\r')
n=int(input())
pat5(n)
