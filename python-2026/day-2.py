# Data Types in python

int = 10
float = 10.34
str = "Ankit"
bool = True


list = [1,2,3,4]
set = {1,2,3,4}
tuple = (1,2,3,4,5)
dict = {"a":1, "b":2, "c":3}

# Mutable vs Immutable
# 1. Immutable (int, float, str, bool)
x = 10
x = x+1
print(x)

# A new object (11) was created, x now points to it, 10 remains unchanged in memory

# Same with strings:
name = "Ankit"
name = name + " Ojha"
print(name)

# Mutable Example (list)
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)
# 4 is added at the end of the string