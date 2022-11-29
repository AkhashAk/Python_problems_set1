def num(arg1):
    num1 = list(str(arg1))
    return "The 1st and last digits are ",int(num1[0])," and ",int(num1[len(num1)-1])
n=int(input())
print(num(n))