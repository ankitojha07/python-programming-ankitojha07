# All basics

from re import match


x = 10
if x> 5:
    print("x is greater than 5")
else:
    print("X is a waste of time")

# For loops
print("\nFor Loop in python")
languages = ["Python", "JS",  "Java", "C++","Javascript", "Ruby", "PHP"]
for lang in languages:
    if lang == "JS" or lang == "Javascript":
        print("You got me!")
    else:
        print("Just pass by")

# Range in python (controlled loop)
print("\nRange in python")
for i in range(7):
    if i==3:
        print("\n")
        continue
    if i ==5:
           break
    print(i)

# Variants of Ranges
print("\nRange Variants in python")
range(2,10)
for i in range(2,10):
    print(i)

print("\nRange Variants in python: Steps")
for i in range(2,10,2):
    print(i) 

# While loop in python

z = 10
while z>0:
    print("met")
    z-=1

# Functions

def add(a,b):
    return a+b