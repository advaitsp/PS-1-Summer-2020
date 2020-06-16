import numpy as np

a=np.array(['geeks', 'is', 'me'])

print(np.char.count(a,'geek'))

print(np.char.count(a, 'e'))

print(np.char.rfind(a,'geek'))

print(np.char.rfind(a, 'e'))



import numpy as np

a='1345'

print(np.char.isnumeric(a))

a='1345s'

print(np.char.isnumeric(a))
