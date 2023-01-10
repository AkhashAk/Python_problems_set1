def pat2(n):
    for i in range(0,n):
        for j in range(1,i+1):
            print(j,end=' ')
        print('\r')
n=int(input())
pat2(n)
