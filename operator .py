num1=int(input("enter a number "))
num2=int(input("enter a number "))
symbol=input("enter a symbol ")
if symbol=="+":
    print(num1+num2)
elif symbol=="-":
    print(num1-num2)
elif symbol=="/":
    print(num1/num2)
elif symbol=="*":
    print(num1*num)
elif symbol=="%":
    print(num1%num2)
elif symbol=="//":
    print(num1//num2)
else:
    print("nothing")