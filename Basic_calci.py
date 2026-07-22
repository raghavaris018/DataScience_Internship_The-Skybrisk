a=int(input("Enter First number:"))
b=int(input("ENter Secound number:"))
z=0
print(" Enter A for Add, S for Sub, M for Mult, D for Div ")
n=input("Enter letter:")
if n=="A":
    z=a+b
    print(z)
elif n=="S":
    z=a-b
    print(z)
elif n=="M":
    z=a*b
    print(z)
else:
    z=a/b
    print(z)
    