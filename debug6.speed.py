# Ab aapne speed check kar ke kuch print karna hai:
# Agar 60 se kam hai toh print karna: "Speed kam hai"
# Agar 30 se kam hai toh print karna: "Speed bahot kam hai"
# Agar 100 se zyada hai toh print karo: "Bahot zyada hai"
# if speed < 60:
#     print ("Speed kam hai")
# elif speed < 30:
#     print ("Speed bahot kam hai")
# elif speed > 100:
#     print ("Speed bahot fast hai")

# Isme ek baar speed 20 daal ke dekho aur dekho ki "Speed bahot kam" hai ki
# output aati hai ya nahi. Agar nahi aati toh isko theek karo aur yeh socho


# correction


speed=int(input("enter the speed"))
if speed<30:
    print("speed bahot kam hai")
elif speed<60:
    print("speed kam hai")    
elif speed>100:
    print("speed bhaot jada hai")
else:
    print("nothing")