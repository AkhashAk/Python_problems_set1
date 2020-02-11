def table(n,m):
    for i in range(1,m+1):
        print(n,' x ',i,'=',n*i)
print('Enter the number to get table for it :',end=' ')
n=int(input())
print('Set Limit :',end=' ')
m=int(input())
table(n,m)
    
