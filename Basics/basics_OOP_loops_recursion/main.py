# Loops
items = [1,2,3,4]
for item in items:
  print(item)

for item in range(15):
  print(item)

for index, item in enumerate(items): # enumerate adds the index to the return
  print(index, item)

# break and continue
for item in items:
  if item == 2:
    continue
  elif item == 3:
    break
  print(item)

  
# Classes

class Animal:
  def walk(self):
    print("Walking...")

class Dog(Animal): # inherits from animal
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def bark(self): # self refers to the specific object using the method
    print("woof!")

roger = Dog("Roger", 12)
print(roger.name)
roger.bark()
roger.walk()


# Modules
# every python file is a module
from lib import dog # import from dog.py from lib folder (lib folder needs __init__)
dog.bark()

from lib.dog import bark
bark()

from math import sqrt
print(sqrt(4))


# Accepting Arguments from command line
"""import sys
name = sys.argv[1] 
print("Hello " + name)"""
# FOR ABOVE: python main.py input

# specify that they have to add an argument when running, like "python main.py -c red"
"""import argparse
parser = argparse.ArgumentParser(
  description="This program prints the name of my dogs"
)
parser.add_argument('-c', '--color', metavar='color', required=True, help='the color to search for')
args = parser.parse_args()
print(args.color)"""


# Lambda Functions
lambda num : num * 2
multiply = lambda a, b : a * b
print(multiply(2,4))


# map(), filter(), reduce()
numbers = [1,2,3,4,5]

result = map(lambda a : a * 2, numbers)
print(list(result))
# original list is untouched!

newResult = filter(lambda n : n % 2 == 0, numbers)
print(list(newResult))
# adds to list if it's True

expenses = [
  ('Dinner', 80),
  ('Car repair', 120)
]
# say we want to sum the expenses
from functools import reduce
sum = reduce(lambda a, b: a[1] + b[1], expenses)
print(sum)


# Recursion
def factorial(n): # python halts recursions at 1000 calls
  if n==1: return 1
  return n * factorial(n-1)
print(factorial(3))


# Decorators

def logtime(func):
  def wrapper():
    print("before")
    val = func()
    print("after")
    return val
  return wrapper
  
@logtime
def hello():
  print('hello')

hello()


# Docstrings
def increment(n):
  """Increment a number"""
  return n + 1
# python processes the triple string
# print(help(increment))


# Annotations
def increment(n: int) -> int:
  # specify that the function receives and returns an int
  return n+1
count: int = 0


# Exceptions
try:
  result = 2/0
except ZeroDivisionError:
  print('cannot divide by zero')
finally:
  result = 1

try:
  raise Exception('An error!')
except Exception as error:
  print(error)

class DogNotFoundException(Exception):
  print('inside')
  pass # means nothing, required placeholder

try: 
  raise DogNotFoundException()
except DogNotFoundException:
  print("Dog not found!")


# with
'''with open(filename, 'r') as file:
   content = file.read()
   print(content)'''


# pip
# go to pypi.org. Pip allows you to download these packages
# pip install, pip uninstall, pip show


# List Compressions
numbers = [1,2,3,4,5]
numbers_power_2 = [n**2 for n in numbers]
print(numbers_power_2)


# Operator Overloading
class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __gt__(self, other):
    return True if self.age > other.age else False

roger = Dog('Roger', 8)
syd = Dog('Syd', 7)

print(roger > syd)

# also works with __add__, __sub__, __mul__, etc