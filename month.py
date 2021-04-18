month=input("enter a month ")
if month=="january" :
    print("its january")
    day=int(input("enter a days "))
    if days<=31:
        print("in january have 31 days")
    else:
        print("total days")
elif month=="febuary":
    print("its febuary month its have 28 days")
    days=int(input("enter a days "))
    if days<=28:
        print("yes its febuary its have 28 days")
    else:
        print("in febuary no up to 29 days")
elif month=="march":
    print("its march")
    days=int(input("enter a days "))
    if days<=31:
        print("in march have 31 days")
    else:
        print("its not march")
elif month=="april":
    print("its april month")
    days=int(input("enter a days "))
    if days<=30:
        print("its april month have 30 days")
    else:
        print("its not april")
elif month=="may":
    print("its may ")
    days=int(input("enter a days "))
    if days<=31:
        print(" may is holiday month ")
    else:
        print("its not holiday month")
elif month=="june":
    print("its june")
    days=int(input("enter a days "))
    if days<=30:
        print("june is rainy month this month have 30")
    else:
        print("its not rainy season")
elif month=="july":
    print("its july")
    days=int(input("enter a days "))
    if days<=31:
        print("july have 31 days ")
    else:
        print("its not july")
elif month=="agust":
    print("its agust month ")
    days=int(input("enter a days "))
    if days<=31:
        print("agust have 31 days")
    else:
        print("its not agust")
elif month=="september":
    print("its september month")
    days=int(input("enter a days "))
    if days<="30":
        print("september have 30 days")
    else:
        print("its not month")
elif month=="octomber":
    print("its octomber month ")
    days=int(input("enter a days "))
    if days<=31:
        print("octomber have 31 days")
    else:
        print("its not a month of 31 days")
elif month=="november":
    print("its november month")
    days=int(input("enter a days "))
    if days<=30:
        print("november have a 30 days ")
    else:
        print("its not month november")
elif month=="december":
    print("its december month")
    days=int(input("enter a days "))
    if days<=31:
        print("december have a 31")
    else:
        print("its last month of year")
else:
    print("nothing")