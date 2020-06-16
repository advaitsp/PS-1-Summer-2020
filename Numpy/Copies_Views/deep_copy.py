import numpy as np 
a = np.array([[10,10], [2,3], [4,5]]) 

print 'Array a is:' 
print a  

print 'Create a deep copy of a:' 
b = a.copy() 
print 'Array b is:' 
print b 

#b does not share any memory of a 
print 'Can we write b is a' 
print b is a  

print 'Change the contents of b:' 
b[0,0] = 100 

print 'Modified array b:' 
print b  

print 'a remains unchanged:' 
print a
