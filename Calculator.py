#Author:- Vriti Shivang
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
print("For adding two numbers Press 1\nFor Subtracting two numbers Press 2\nFor multiplying two numbers Press 3\nFor divison of two numbers Press 4\n")
n=int(input("Enter your choice: "))
if n==1:
    print(a+b)
elif n==2:
    print(a-b)
elif n==3:
    print(a*b)
elif n==4:
    print(a/b)
else:
    print("wrong choice\nTry again")