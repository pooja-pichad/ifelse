# hum ek game banayenge usme hume wining number guess karna hai.
# we have given a one winning number and we have give 5 chance to play game ,
# then show it is lose or win



num=int(input("enter a guss number"))
winning_number=27
if num==winning_number:
    print("you won")
else:
    if num<winning_number:
        print("too low")
    else:
        print("too high")