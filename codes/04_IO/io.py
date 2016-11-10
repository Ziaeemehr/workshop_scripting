#!/usr/bin/python

print raw_input('What is your name? ')

x = raw_input('What is your name?')

f = open('test.txt', 'r')
for line in f:
    print line
f.close()

# The newer and better way to read from a file:
with open("test.txt", "r") as txt:
    for line in txt:
        print line
        
for line in open('test.txt', 'r'):
    print line
    
import sys
for arg in sys.argv[1:]:
  print arg  
  
file1 = open("TestFile.txt","w")
for i in range(1,10+1):
  print >> file1, i
file1.close()


file1 = open("TestFile.txt","w")
for i in range(1,10+1):
  if i>1:
    file1.write("-")
  file1.write(str(i))
file1.close()