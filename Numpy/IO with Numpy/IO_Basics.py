#save()
import numpy as np 

a = np.array([1,2,3,4,5]) 
np.save('outfile',a)

#load()
import numpy as np 
b = np.load('outfile.npy') 
print b 

#savetxt()
import numpy as np 

a = np.array([1,2,3,4,5]) 
np.savetxt('out.txt',a) 
b = np.loadtxt('out.txt') 
print b 
