# a simple calculator using(/,*,-,+)
num1=int(input("enter first number"))
num2=int(input("enter second number"))

print("enter the operation you would like to perform")
ch=input("enter any of these char for spesific operation +,-,*,/:")

result=0
if ch=='+':
    result=num1 + num2
elif ch=="-":
    result=num1 - num2
elif ch=="*":
    result=num1 * num2
elif ch=="/":
    result=num1 / num2
else:
    print("input character is not recorgnised!")

print(num1, ch, num2, ":",result )  