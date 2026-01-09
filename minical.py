a=int(input("A:"))
b=int(input("B:"))
operation=input("Add/Sub/Mul/Div:")
if(operation=="Add"):
    print(a+b)
elif(operation=="Sub"):
    print(a-b)
elif(operation=="Mul"):
    print(a*b)
elif(operation=="Div"):
    print(a/b)
else:
    print("Invalid error")
