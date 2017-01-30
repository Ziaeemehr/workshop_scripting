#!/usr/bin/python

#list.append(obj)

aList = [123, 'xyz', 'zara', 'abc'];
aList.append( 2009 );
print "Updated List : ", aList

aList = [123, 'xyz', 'zara', 'abc', 123];
print "Count for 123 : ", aList.count(123)

aList = [123, 'xyz', 'zara', 'abc', 123];
bList = [2009, 'manni'];
aList.extend(bList)
print "Extended List : ", aList 
import random
aList = [0,8,6,9,5,1,10,88]
aList.sort();
print "List : ", aList
