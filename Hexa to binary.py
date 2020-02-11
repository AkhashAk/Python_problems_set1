def hex_tobinary(n):
    d= str(int(n,16))
    decm = int(d)
    return print(n,"in Binary is ", bin(decm))
n=input()
print(hex_tobinary(n))
