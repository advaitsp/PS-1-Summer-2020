import numpy as np 
a = np.array([-5.6j, 0.2j, 11. , 1+1j]) 

print 'Our array is:' 
print a 
print '\n'  

print 'Applying real() function:' 
print np.real(a) 
print '\n'  

print 'Applying imag() function:' 
print np.imag(a) 
print '\n'  

print 'Applying conj() function:' 
print np.conj(a) 
print '\n'  

print 'Applying angle() function:' 
print np.angle(a) 
print '\n'  

print 'Applying angle() function again (result in degrees)' 
print np.angle(a, deg = True)
