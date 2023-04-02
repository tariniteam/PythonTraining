
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

