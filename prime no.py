num=int(input("enter the number"))
if num==2 or num==3 or num==5 or num==7:
    print("it is prime number ")
elif num%2==0 or num%3==0 or num%5==0 or num%7==0:
    print("it is not prime number")
else:
    print(num,"it is prime number")
