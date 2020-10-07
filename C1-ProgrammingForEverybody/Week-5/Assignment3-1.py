#To calculate gross pay by taking input from user
# IF hour is more than 40 pay would be 1.5 times

#input
hrs = input("Enter the no. of hours: ")
rate = input("Enter the Hourly Rate: ")

#convert
h = float(hrs)
r = float(rate)

#print(h, r)
#Condition to check hours and adding the extra Hours
if h > 40 :
    extra = h - 40
#print("Extra: ", extra)

grosspay = ((h - extra) * r) + extra * (r * 1.5)

print(grosspay)

input("End - Please Exit")
