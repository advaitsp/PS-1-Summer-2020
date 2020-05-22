# Removing Elements From a Dictionary
# Initial Dictionary 
Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Python', 
		'A' : {1 : 'Python', 2 : 'For', 3 : 'Everyone'}, 
		'B' : {1 : 'Python', 2 : 'Life'}} 
print("Initial Dictionary: ") 
print(Dict) 

# Deleting a Key value 
del Dict[6] 
print("\nDeleting a specific key: ") 
print(Dict) 

# Deleting a Key from 
# Nested Dictionary 
del Dict['A'][2] 
print("\nDeleting a key from Nested Dictionary: ") 
print(Dict) 
