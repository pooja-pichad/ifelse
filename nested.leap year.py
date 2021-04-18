# leap year 
# we have take one user input and show  the year its leap year or not 



year=int(input("enter a year"))
x=("%d",year)
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("it is a leap year",year)
        else:
            print("  no its not a leap year ")
    else:
        print(" leap year")        
else:
    print(" not leap year")
    
