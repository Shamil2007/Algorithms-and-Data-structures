# Let's create a simple array (list in Python)
string = ['a', 'b', 'c', 'd']

# Access an element by index (constant time complexity: O(1))
# Explanation: Python lists allow direct access to elements by their index
var = string[3]  # Access the 4th element (index 3)
print("Accessed element at index 3:", var)  # Output: d

# Push (append an element to the end of the list) - O(1) average time
# Explanation: Appending at the end is typically constant time as Python lists over-allocate memory.
string.append('e')
print("After append:", string)  # Output: ['a', 'b', 'c', 'd', 'e']

# Pop (remove the last element) - O(1) time
# Explanation: Removing the last element is constant time as no elements need to shift.
string.pop()
print("After pop:", string)  # Output: ['a', 'b', 'c', 'd']

# Insert an element at the beginning (index 0) - O(n) time
# Explanation: Inserting at index 0 requires shifting all elements one position to the right.
string.insert(0, '-1')
print("After insert at beginning:", string)  # Output: ['-1', 'a', 'b', 'c', 'd']

# Delete an element at a specific position (e.g., index 2) - O(n) time
# Explanation: Deleting at an index (other than the end) requires shifting all elements to the left.
del string[2]
print("After deleting element at index 2:", string)  # Output: ['-1', 'a', 'c', 'd']
