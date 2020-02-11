def hex_tooct(n):
    d= str(int(n,16))
    decm = int(d)
    return print(n, "in Octal is ", oct(decm))
n=input()
hex_tooct(n)
