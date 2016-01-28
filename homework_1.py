# Catarina Soeiro
# January 26 2016
# homework_1.py

##### Template for Homework 1, exercises 1.2-1.5 ######

# Do your work for Exercise 1.2 here

print " | | "
print "-----"
print " | | "
print "-----"
print " | | "

print "********** Exercise 1.3 **********"

a = " | | "
b = "-----"
print a
print b
print a
print b
print a

print "********** Exercise 1.4 **********"
print "********* Part II *************"

a = (3*5)/(2+3)
print "a is " + str(a)
b = ((7+9)**0.5)*2
print "b is " + str(b)
c = (4-7)**3
print "c is " + str(c)
d = (-19+100)**0.25
print "d is " + str(d)
e = 6 % 4
print "e is " + str(e)

print "********* Part III *************"

#assign equations to variable names
e1 = (3+4)*5+(-10/2)
e2 = (3+4*5)+(-10/2)

#print result
print e1
print e2

print "********** Exercise 1.5 **********"

#collect name info from user
name1 = raw_input('Enter your first name: ')
name2 = raw_input('Enter your last name: ')

#collect birth date from user
print 'Enter your date of birth:'
mo = raw_input('Month? ')
day = raw_input('Day? ')
year = raw_input('Year? ')

#print result
print name1, name2, 'was born on', mo, day+',', year+'.'
