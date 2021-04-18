time=float(input("enter the time"))
if time>6.00 and time<=7.00 :
    print("morning excercise")
elif time>7.00 and time<=8.30:
    print("nasta time")
elif time>8.30 and time<=9.30:
    print("english activity")
elif time>9.30 and time<=13.0:
    print("coding time")
elif time>13.0 and time<=14.30:
    print("lunch time")
elif time>15.30 and time<=17.30:
    print("study time")
elif time>17.30 and time<=18.0:
    print("break time ")
elif time>18.0 and time<=20.0:
    print("study time")
elif time>20.0 and time<=22.0:
    print("dinnar time")
else:
    print("sleep")