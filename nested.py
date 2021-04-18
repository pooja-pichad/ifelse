age=int(input("enter the age"))
if age>=18:
    print("age is valid")
    education=(input("enter your education"))
    if education=="graduation":
        print("you are education is valid")
        experience=(input("enter your experience"))
        if experience=="yes":
            print("you are eligible for job ")
        else:
            print("you have no experience so you are not eligible for job ")
    else:
        print("you are education is less so you are not eligible for job ") 
else:
    print("you are age is not valid")                   