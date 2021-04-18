alphabate=input("enter a alphabate")
if alphabate>="a" or alphabate<="z":
    print(alphabate)
    cha=input("enter a character")
    if cha=="@" or cha=="#" or cha=="$" or cha=="&":
        print(cha)
        num=int(input("enter a number"))
        if num>=0:
            print(alphabate+cha+str(num))
        else:
            print("incorrect number")
    else:
        print("incorrect character")
else:
    print("incorrect alphabate")