marks=int(input("enter a marks "))
varx=marks/100*100
if varx>=90:
    print( varx,"grade A")
elif varx>=80:
    print(varx,"grade B")
elif varx>=60:
    print(varx,"grade C")
elif varx>=50:
    print(varx,"grade D")
elif varx>=40:
    print(varx,"grade E")
elif varx<40:
    print("fail")
else:
    print("not greater")
