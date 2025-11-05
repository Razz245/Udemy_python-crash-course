# Class 13: Python Sets
# ---------------------
# A set is an unordered collection of unique elements in Python.
# It is mutable but does not allow duplicate values.

# 🔹 Creating a set
numbers = {1, 2, 3, 4, 5}
print("Original set:", numbers)

# 🔹 Adding elements
numbers.add(6)
print("After adding 6:", numbers)

# 🔹 Removing elements
numbers.remove(3)  # Will raise an error if 3 is not found
print("After removing 3:", numbers)

# 🔹 Using discard() (no error if element not found)
numbers.discard(10)
print("After discarding 10:", numbers)

# 🔹 Set operations
even = {2, 4, 6, 8}
odd = {1, 3, 5, 7}

# Union
print("Union:", even.union(odd))

# Intersection
print("Intersection:", numbers.intersection(even))

# Difference
print("Difference:", numbers.difference(even))

# Symmetric Difference
print("Symmetric Difference:", even.symmetric_difference(odd))

# 🔹 Clearing a set
numbers.clear()
print("After clearing:", numbers)

# 🔹 Set from a list (to remove duplicates)
list_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(list_with_duplicates)
print("Unique set from list:", unique_set)
