#Write a program to read through the mbox-short.txt and figure out who has sent
# the greatest number of mail messages. The program looks for 'From ' lines and
# takes the second word of those lines as the person who sent the mail. The
# program creates a Python dictionary that maps the sender's mail address to a
# count of the number of times they appear in the file. After the dictionary is
# produced, the program reads through the dictionary using a maximum loop to
# find the most prolific committer.

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

idwords = dict()

try :
    fh = open(fname)
except :
    print('Enter Proper File name : ', fname)
    input("End")

bigword = None
bigcount = 0

for line in fh:

    if not line.startswith("From:"):
        continue

    line.rstrip()
    y = line.split()
    ids = y[1]
    if ids in idwords :
        idwords[ids] = idwords[ids] + 1
        if idwords[ids] > bigcount:
            bigcount = idwords[ids]
            bigword = ids

    else:
        idwords[ids] = 1

print(bigword,bigcount)
