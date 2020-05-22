import array as arr

numbers = arr.array('i', [1, 2, 3, 5, 7, 10])

# changing first element
numbers[0] = 0    
print(numbers)   

# changing 3rd to 5th element
numbers[2:5] = arr.array('i', [4, 6, 8])   
print(numbers)  