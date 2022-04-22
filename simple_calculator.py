a=int(input("enter first operand "))
b=int(input("enter second operand "))
o=input("enter operand")
if o=='*':
    print(a*b)
elif o=='+':
    print(a+b)
elif o=='-':
    print(a-b)
elif o=='/' :
    print(a/b)
else:
    print("not an operator")
