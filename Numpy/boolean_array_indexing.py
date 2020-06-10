import numpy as np 
x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]]) 

print 'Our array is:' 
print x 
print '\n'  

# Now we will print the items greater than 5 
print 'The items greater than 5 are:' 
print x[x > 5]
 
import numpy as np 
a = np.array([np.nan, 1,2,np.nan,3,4,5]) 
print a[~np.isnan(a)]

# filter out the non-complex elements from an array
import numpy as np 
a = np.array([1, 2+6j, 5, 3.5+5j]) 
print a[np.iscomplex(a)]
