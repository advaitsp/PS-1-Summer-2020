import numpy as np 
a = np.array([[30,40,70],[80,20,10],[50,90,60]]) 

print 'Our array is:' 
print a 
print '\n' 

print 'Applying argmax() function:' 
print np.argmax(a) 
print '\n'  

print 'Index of maximum number in flattened array' 
print a.flatten() 
print '\n'  

print 'Array containing indices of maximum along axis 0:' 
maxindex = np.argmax(a, axis = 0) 
print maxindex 
print '\n'  

print 'Array containing indices of maximum along axis 1:' 
maxindex = np.argmax(a, axis = 1) 
print maxindex 
print '\n'  

print 'Applying argmin() function:' 
minindex = np.argmin(a) 
print minindex 
print '\n'  
   
print 'Flattened array:' 
print a.flatten()[minindex] 
print '\n'  

print 'Flattened array along axis 0:' 
minindex = np.argmin(a, axis = 0) 
print minindex
print '\n'

print 'Flattened array along axis 1:' 
minindex = np.argmin(a, axis = 1) 
print minindex
