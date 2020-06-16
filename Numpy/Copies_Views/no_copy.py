import numpy as np 
a = np.arange(6) 

print 'Our array is:' 
print a  

print 'Applying id() function:' 
print id(a)  

print 'a is assigned to b:' 
b = a 
print b  

print 'b has same id():' 
print id(b)  

print 'Change shape of b:' 
b.shape = 3,2 
print b  

print 'Shape of a also gets changed:' 
print a
