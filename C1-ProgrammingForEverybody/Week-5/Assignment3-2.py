#To assign grades based on marks entered

#input
score = input("Enter the Score in between 0.0 to 1.0: ")

#convert and check
try :
    scr = float(score)
except:
    input("Enter Numeric Value")
    quit()

#print("Score= " ,scr)

# Check value in between 0 and 1
try :
    scr >= 0.0
except :
    input("Enter Value between 0 and 1")
    quit()

try :
    scr <= 1.0
except :
    input("Enter Value between 0 and 1")
    quit()

if scr>=0.9 :
    print("A")
elif scr>=0.8 :
    print("B")
elif scr>=0.7 :
    print("C")
elif scr>=0.6 :
    print("D")
else :
    print("F")

input("Press enter to end")
