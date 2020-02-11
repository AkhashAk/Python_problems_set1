def pat4(n):
    k=n-2
    for i in range(n,0,-1):
        for j in range(0,k):
            print(end=' ')
        k=k+1
        for j in range(0,i):
            print("* ",end='')
        print('\r')
    print(end='')
    for i in range(0,n):
        for j in range(0,k-1):
            print(end=' ')
        k=k-1
        for j in range(0,i+1):
            print("* ",end='')
        print("\r")
n=int(input())
pat4(n)
