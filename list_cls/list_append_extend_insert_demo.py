lst = ['A', 'B']
print(f"List is : {lst}")

# List Append method
lst.append("D")
print(f"List is : {lst}")
# ['A', 'B', 'D']

# List Append method
lst.append(["E", "F"])
print(f"List is : {lst}")
# ['A', 'B', 'D', ['E', 'F']]

# List insert method
lst.insert(2, "C")
print(f"List is : {lst}")
# ['A', 'B', 'C', 'D', ['E', 'F']]

# List extend method
lst.extend(["G", "H"])
print(f"List is : {lst}")
# ['A', 'B', 'C', 'D', ['E', 'F'], 'G', 'H']