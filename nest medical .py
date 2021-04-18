medicalcause=input("enter a cause ")
classheld=int(input("enter a number of class held"))
classattended=int(input("enter a number of class attended"))
varx=classattended/classheld*100
if medicalcause=="y":
    print(" yes allowed")
    if varx>=75:
        print("allowed for exam")
    else:
        print("not allowed for exam ")
else:
    print("not allowed")