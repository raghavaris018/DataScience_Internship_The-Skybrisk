a=int(input("Enter First number:"))
b=int(input("ENter Secound number:"))
operator=input("Enter Operator:")
if operator=="+":
    print(f"Addition of two numbers:{a+b}")
elif operator=="-":
    print(f"Subtraction of two numbers:{a-b}")
elif operator=="*":
    print(f"Multiplication of two numbers:{a*b}")
elif operator=="/":
    print(f"Division of two numbers:{a/b}")
else:
    print("invalid Operator")
    