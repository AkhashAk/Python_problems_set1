def swap():
    l=[12345]
    l=list(map(int, str(l[0])))
    t=[]
    print(l[0])
    t=l[0]
    l[0]=l[len(l)-1]
    l[len(l)-1]=t
    return print(l)
swap()
