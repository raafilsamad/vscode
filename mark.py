score=int(input("enter your score within 100:"))
if(score<35):
    print("Poor student")
elif(score>35 and score<70):
    print("average student")
if(score>70):
    print("Good student")
else:
    print("study more")