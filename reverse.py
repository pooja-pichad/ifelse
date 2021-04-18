n=int(input("enter any number"))
a=n%10
b=(n//10)%10
c=(n//100)%10
if n>0:
    print((a*100)+(b*10)+(c*1))
else:
    print("not") 