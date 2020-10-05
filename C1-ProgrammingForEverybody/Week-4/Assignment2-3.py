# Program to calculate the payroll based on rate and hours

# input
hrs = input("Enter Hours: ")
rate = input("What is the rate per hour: ")

#Convert
fhrs = float(hrs)
frate = float(rate)

#Calculate
pay = fhrs * frate


#Print Output
print('Pay:', pay)

input("End - Please Exit")
