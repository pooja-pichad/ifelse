# we have to check whether the number is divisibal by 3 and then show "fizz".
# and its divisibal by 5 then show "buzz".the number is divisible by both then show 
# "fizzbuzz".





num=int(input("enter a number"))
if num%3==0 and num%5==0:
    print("fizz-buzz")
elif num%3==0:
    print("fizz")
elif num%5==0:
    print("buzz")
else:
    print("buzz fizz")