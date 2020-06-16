import numpy as np 

nm = ('raju','anil','ravi','amar') 
dv = ('f.y.', 's.y.', 's.y.', 'f.y.') 
ind = np.lexsort((dv,nm)) 

print 'Applying lexsort() function:' 
print ind 
print '\n'  

print 'Use this index to get sorted data:' 
print [nm[i] + ", " + dv[i] for i in ind] 
