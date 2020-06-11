# nditer object has another optional parameter called op_flags.
import numpy as np
a = np.arange(0,60,5)
a = a.reshape(3,4)
print 'Original array is:'
print a
print '\n'

for x in np.nditer(a, op_flags = ['readwrite']):
   x[...] = 2*x
print 'Modified array is:'
print a

# one-dimensional arrays corresponding to each column 
# is traversed by the iterator.
import numpy as np 
a = np.arange(0,60,5) 
a = a.reshape(3,4) 


print 'Original array is:' 
print a 
print '\n'  


print 'Modified array is:' 
for x in np.nditer(a, flags = ['external_loop'], order = 'F'):
   print x,
