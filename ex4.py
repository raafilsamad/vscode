english=int(input("enter the marks for english:"))
tamil=int(input("enter the marks for tamil:"))
maths=int(input("enter the marks for maths:"))
science=int(input("enter the marks for science:"))
social=int(input("enter the marks for social:"))
average=english+tamil+maths+science+social/5
print(average)
if(average<30):
    print("additional class required")
else:
    print("you are good to go!")
