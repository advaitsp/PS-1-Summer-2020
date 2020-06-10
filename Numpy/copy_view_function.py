 
import numpy as np
a=np.array([1,2,3,4])
x=a.copy()
y=a.view()

x[0]=42
print(x)
print(a)
y[0]=42

print(y)
print(a)

a[0]=37

print(x)
print(y)
print(x.base)
#none bcoz it is copy
print(y.base)
#array a is its base
© 2020 GitHub, Inc.
