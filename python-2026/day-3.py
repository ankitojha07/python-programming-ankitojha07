# All basics

import numbers
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

# Keyword Arguments (Python Superpower)
def create_user(name, role, active= True):
    return {
        "name":name,
        "role":role,
        "isActive":active
    }

user = create_user("Ankit", "ASC", False)
user2 = create_user(role="ASC",name="Rohit", active=True)
print(user)
print(user2)

# *args and **kwargs (Flexible Functions)
## *args → multiple positional arguments
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1,2,3,4,5))

## **kwargs → key-value arguments
def log_events(**data):
    return data
print(log_events(user="Ankit", action="login", role="ASC"))

# Returning Multiple Values (Pythonic)
def get_user():
    name = "Test 1"
    role = "Role 1"
    return name, role

name, role = get_user()
print(name, role)

# Function Annotations (Modern Python – 2026 Standard)
def calculate_salary(base:int, bonus:int) -> int:
    return base+bonus
print(calculate_salary(1,2))

def process_payment(amount:float, currency:str="INR") -> dict:
    if amount <= 0:
        return {"Status":"failed", "reason":"Invalid Amount"}
    return{
        "status":"success",
        "amount":amount,
        "currency":currency
    }
print(process_payment(500))
print(process_payment(0))

def register_user(name, role="user", **metaData):
    return{
        "name":name,
        "role":role,
        **metaData
    }

print(register_user("Ankit"))
print(register_user("Ankit", "Tester"))
print(register_user("Ankit","QA", email="ankit.ojha@leena.ai", age=24))
print(register_user("Ankit", email="ankit.ojha@leena.ai", age=24))

# List in python - Ordered, Mutable (Most Used)
nums = [1,2,3,4,5]
nums.append(8)
print(nums)

nums.remove(5)
print(nums)

nums.pop()
print(nums)

# tuple - Ordered, Immutable
coordinates = (10,20)
x,y= coordinates
print(x,y)

# set – Unique, Unordered
ids = {1, 2, 3, 3, 4}
print(ids)

ids.add(13)
print(ids)

ids.remove(1)
print(ids)

## powerful set logics
a = {1,2,3}
b = {3,4,5}
print(a & b)
print(a | b)
print(a - b)

# dict – Key-Value Store (MOST IMPORTANT)
user = {
    "name":"Ankit Ojha",
    "role":"engineer",
    "active":True
}

user["role"] = "Senior Engineer"
print(user)

user["experience"] = 4
print(user)

## Safe Access
print(user.get("email")) # none if missing email
print(user.get("role")) # Senior Engineer

# Nested Structures (Real World)
users = [
    {"name": "Ankit", "role": "Engineer"},
    {"name": "Rahul", "role": "Manager"}
]

print(users[1]["name"])