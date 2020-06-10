# an array of evenly spaced numbers 
import numpy as np 
a = np.arange(24) 
print a

# this is one dimensional array 
import numpy as np 
a = np.arange(24) 
a.ndim  

# now reshape it 
b = a.reshape(2,4,3) 
print b 
# b is having three dimensions
