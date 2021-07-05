message1 = '{0} is easier than {1}'.format('Python', 'Java')
message2 = '{1} is easier than {0}'.format('Python', 'Java')
message3 = '{:10.2f} and {:d}'.format(1.234234234, 12)
message4 = '{}'.format(1.234234234)
print (message1)
print (message2)
print (message3)
print (message4)


car = '{0} and {1} is a car'.format('Mini', 'BMW')
print (car)
 
nofloaty = 'here is a float 1.234234234 here is the float as a precison of 3 number {:0.2f}  {:s} {:d} {:d}'.format(1.234234234, 'h', 12, 14)
print (nofloaty)
