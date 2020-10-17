# 10.2 Write a program to read through the mbox-short.txt and figure out the
# distribution by hour of the day for each of the messages. You can pull the hour
# out from the 'From ' line by finding the time and then splitting the string a
# second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts,
# sorted by hour as shown below.


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"

hourcount = dict()

try :
    handle = open(name)
except :
    print('Enter Proper File name : ', name)
    input("End")

bighour = None
bigcount = None

for line in handle:

    if not line.startswith("From "):
        continue


    y = line.split()
    line.rstrip()
    y = line.split()
    hour = y[5].split(':')
    hrs = hour[0]

    if hrs in hourcount:
        hourcount[hrs] = hourcount[hrs] + 1
    else:
        hourcount[hrs] = 1

#print(hourcount)

lst = list()
for key,val in hourcount.items():
    newtup = (key,val)
    lst.append(newtup)

lst = sorted(lst)

for key,val in lst:
    print(key,val)
