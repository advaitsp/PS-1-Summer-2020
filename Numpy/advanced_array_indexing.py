import numpy as np 
x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]]) 
   
print 'Our array is:' 
print x 
print '\n' 

rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]]) 
y = x[rows,cols] 
   
print 'The corner elements of this array are:' 
print y



import numpy as np 
x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]]) 

print 'Our array is:' 
print x 
print '\n'  

# slicing 
z = x[1:4,1:3] 

print 'After slicing, our array becomes:' 
print z 
print '\n'  

# using advanced index for column 
y = x[1:4,[1,2]] 

print 'Slicing using advanced index for column:
