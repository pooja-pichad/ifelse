day=input("enter a day")
if day=="thusrday":
    print("today is holiday")
    permission=input("write a permission")
    if permission=="yes":
        print("yes we are go to outside")
        precaution=input("write a precaution")
        place=input("write a place")
        if precaution=="mask and sanitizer" and place=="canteen":
            print(" permission hai bring mask and sanitizer and go to canteen")
        else:
            print("do not go any were")
    else:
        print("no permission")
else:
    print("any day")                

       