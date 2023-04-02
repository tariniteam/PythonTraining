
#Memory Reference of list 

# Suppose the elements of the list 'ls' are stored at random location with random address stated below in the format :
# variable_name = value --> address of random location
# Memory Reference of independent variable through id function may generate somthing list this 
# ID of a: 838956116272
# ID of b: 838956116304
# ID of c: 838961629360
# ID of d: 838961295536

# Memory Reference of list items through id function will generate same memory reference as of indipendent variable ref
# ID of lst[0]: 838956116272
# ID of lst[1]: 838956116304
# ID of lst[2]: 838961629360
# ID of lst[3]: 838961295536

# Memory Reference of list id function
# ID of lst: 838961366656

a = 1
b = 2
c = 'Testing'
d = '1.1'

lst = [a,b,c,d]

# Memory Reference of independent variable through id function
print("Memory Reference of independent variable through id function")
print(f"ID of a: {id(a)}")
print(f"ID of b: {id(b)}")
print(f"ID of c: {id(c)}")
print(f"ID of d: {id(d)}")

print("\nMemory Reference of list items through id function")
print(f"ID of lst[0]: {id(lst[0])}")
print(f"ID of lst[1]: {id(lst[1])}")
print(f"ID of lst[2]: {id(lst[2])}")
print(f"ID of lst[3]: {id(lst[3])}")

print("\nMemory Reference of list id function")
print(f"ID of lst: {id(lst)}")

#Since the list are mutable lets change item value of list 
print("\nChanging the 3rd item of list")
lst[2] = "Test Done"
print(f"List changed to : {lst}")

print("Lets see the change impact in the mem reference of second item")
print(f"ID of lst[0]: {id(lst[0])}")
print(f"ID of lst[1]: {id(lst[1])}")
print(f"ID of lst[2]: {id(lst[2])}")
print(f"ID of lst[3]: {id(lst[3])}")

print("\nLet declare a variable with the same value as list 2nd item and see the mem ref")
x = lst[2]
print(f"Mem Reference of x is: {id(x)}")
print(f"ID of lst[2]: {id(lst[2])}")

# x = ['a', 'b', 'c']
# print(id(x[0]))             -> 01014518
# print(id(x[1]))             -> 01014528
# print(id(x[2]))             -> 01014556

# print(id(x))                -> 18458914**