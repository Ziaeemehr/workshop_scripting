while True:
    try:
        x = int(raw_input("Please enter a number: "))
        break
    except ValueError:
        print "Oops!  That was no valid number.  Try again..."

#handling error for reading a file        
import os
if os.path.exists(fName):
   with open(fName, 'rb') as f:
       try:
           # do stuff
       except : # whatever reader errors you care about
           # handle error
#-----------------------------------------------------           
if os.path.exists(fName):
   with open(fName, 'rb') as f:
       try:
           # do stuff
       except : # whatever reader errors you care about
           # handle error
#-----------------------------------------------------
try:
    f = open(fname, 'r')
except IOError:
    print "Could not read file:", fname
    sys.exit()
with f:
    reader = csv.reader(f)
    for row in reader:
        pass #do stuff here
