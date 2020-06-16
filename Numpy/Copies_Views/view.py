import numpy as np 
# To begin with, a is 3X2 array 
a = np.arange(6).reshape(3,2) 

print 'Array a:' 
print a  

print 'Create view of a:' 
b = a.view() 
print b  

print 'id() for both the arrays are different:' 
print 'id() of a:'
print id(a)  
print 'id() of b:' 
print id(b)  

# Change the shape of b. It does not change the shape of a 
b.shape = 2,3 

print 'Shape of b:' 
print b  

print 'Shape of a:' 
print a
