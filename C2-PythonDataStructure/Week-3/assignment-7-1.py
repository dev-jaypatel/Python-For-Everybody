# 7.2 Write a program that prompts for a file name, then opens that file and
# reads through the file, looking for lines of the form:
# -DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines
# and compute the average of those values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
# when you are testing below enter mbox-short.txt as the file name.


# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"


count = 0

try :
    fh = open(fname)
except :
    print('Enter Proper File name : ', fname)
    input("End")

for line in fh:
    line.strip()

    if not line.startswith("From"):
        continue

    line.split(" ")
    print(line)
    count += 1

print("There were", count, "lines in the file with From as the first word")

input("end")
