num1=int(input("enter the number"))
num2=int(input("enterthe number"))
num3=int(input("enter the number"))
if num1==num2==num3:
    print("equilateral")
elif (num1==num2!=num3) or (num1!=num2==num3) or (num1==num3!=num2) :
    print("isoscales triangle")
else:
    print("scalen trIangle")  