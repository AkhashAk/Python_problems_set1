def ascii_char(n):
    while(n>=0 and n<=127):
        print('The ASCII character ',chr(n),"'s value is ",n)
        n+=1
n=0
ascii_char(n)
