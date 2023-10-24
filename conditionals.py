num = int(input("Enter Number : "))

if num > 0:
    print(f"{num} is positive")
else:
    print(f"{num} is Negative Number")

Age = int(input("Enter Age to Vote: "))
if Age>=18 and Age<=80:
    print("You are Eligible to Vote")
else:
    print("You can't Vote Because you are a Minor")