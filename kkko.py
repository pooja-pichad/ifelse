n = int(input("Please enter the amount of rows: "))
i = 0
while(i <= n):
    spaces = n -i
    j = 0
    while(j <=spaces): #j is defined a space counter
        print(" ", end='')
        j =j +1
        stars = 2*i-1
    while(stars > 0):
        print("*", end='')
        stars =stars-1 
    print()
    i=i+1