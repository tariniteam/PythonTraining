from sys import getsizeof

# A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements. Each element or 
# value that is inside of a list is called an item

#Memory Allocation in list: Intially when we create list it occupy 56 byte of space which is C structure object allocation, 
# with first assignment it first increase the size to 32 byte which is equal to 4 int value, which means for next four int 
# element there wont be any memory allocation in list   

#Empty List
l = []
print(l)
print(f"Mem with empty list: {getsizeof(l)}")

#Append 1st Element
l.append(1)
print(l)
print(f"Mem with one item in list: {getsizeof(l)}")

#Append 2nd Element
l.append(2)
print(l)
print(f"Mem with one item in list: {getsizeof(l)}")

#Append 3rd Element
l.append(3)
print(l)
print(f"Mem with one item in list: {getsizeof(l)}")

#Append 4th Element
l.append(4)
print(l)
print(f"Mem with one item in list: {getsizeof(l)}")

#Now we are adding 5th element, and as per our calculation there is no addition space left in list to store this new 5th 
# element, so it sould now add 32 byte to the existing space to accomodate next 4*8byte info

#Append 5th Element
l.append(5)
print(l)
print(f"Mem with one item in list: {getsizeof(l)}")


del(l)


