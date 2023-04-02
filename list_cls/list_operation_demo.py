
# 1) Checking if the list is  empty.
lst = []
print("\nChecking if the list is empty")
print(f"List: {lst}")
if not lst:
    print("List is empty")

print("Other way to check if the list is empty")
if  len(lst) == 0:
    print("List is empty")


# 2) One line assignment of if condition if list 
print("\nOne liner assignment if condtion matchs or not matchs")
lst_empty = True if not lst else False
print(lst_empty)

# 3) Finding an index of an item in list
lst2 = ['a','b','c','d','e']
index_a = lst2.index('d')
print(f"Index of d in the list is: {index_a}")


#Index only return first occurance of matched item index
# A call to index searches through the list in order until it finds a match, and stops there. 
# If there could be more than one occurrence of the value, and all indices are needed, index cannot solve the problem
lst2.append('d')
print(f"List items: {lst2}")
index_a = lst2.index('d')
print(f"Index of d in the list is: {index_a}")

#To find all the occurance of matched item, we can use enumerate 
print('\nEnumerate way of finding the index of matched item')
for indx, item in enumerate(lst2):
    if item == 'd':
        print(f'The index of matched item is: {indx}')

#To find the all matching occurance using list comprehansion
lst = [idx for idx, v in enumerate(lst2) if v == 'd']
print(f"Matching index list is: {lst}")

#Using Generator to find the matching occurance
g = (i for i, v in enumerate(lst2) if v == 'd')
print(f"The index is {next(g)}") 
print(f"The index is {next(g)}") 

#Finding he length of list using __len__() and len function
print(f"\nFinding the length of list")
lst = ['a','b','c','d']
print(f"Length of list is : {lst.__len__()}")
print(f"Length of list is : {len(lst)}")










