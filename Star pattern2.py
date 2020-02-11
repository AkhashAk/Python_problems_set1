def pat2(n):
    k=n-1
    for i in range(0,n):
        for j in range(0,k):
            print(' ',end='')
        for j in range(0,i+1):
            print('* ',end='')
        k=k-1
        print('\r')
    k=0
    for i in range(0,n):
        for j in range(0,k+1):
            print(' ',end='')
        for j in range(0,n-1):
            print('* ',end='')
        k=k+1
        n=n-1
        print('\r')
n=int(input())
pat2(n)
