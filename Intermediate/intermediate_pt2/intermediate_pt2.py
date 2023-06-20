# Random numbers (psuedo random)
import random

a = random.random()
b = random.uniform(1, 10) # random float in the range
c = random.randint(1, 10) # includes upper bound
d = random.randrange(1, 10) # does not include upper bound
e = random.normalvariate(0, 1) # random value from normal distribution with (mean, st. dev)

mylist = list("ABCDEFGH")
a = random.choice(mylist) # random element
b = random.sample(mylist, 3) # 3 unique random elements
c = random.choices(mylist, k=3) # above, but repeatable
d = random.shuffle(mylist) # shuffle in place

# psuedo random: different seeds
# can reproduce your data
random.seed(10)
print(random.random())
print(random.randint(1,10))
random.seed(2)
print(random.random())
print(random.randint(1,10))

# generate true random number
# takes more time
import secrets
a = secrets.randbelow(10) # 0 to 10, 10 not included
b = secrets.randbits(4) # i.e. 1010
mylist = list("asdf")
c = secrets.choice(mylist) # random choice

# numpy
# uses different seed from standard library's random
import numpy as np
b = np.random.rand(3) # 3 random floats
print(b)
c = np.random.rand(3,3) # 3 by 3 random floats
print(b)
a = np.random.randint(0, 10, (3,4)) 
print(a)
# np.random.shuffle()

np.random.seed(1)
print(np.random.rand(3,3))
np.random.seed(1)
print(np.random.rand(3,3))


# Decorators
# takes another function as argument, and extends behavior without modifying the original

# Function Decorator
def start_end_decorator(func):
  def wrapper():
    print('Start')
    func()
    print('End')
  return wrapper

@start_end_decorator
def print_name():
  print('Alex')

print_name()
print_name = start_end_decorator(print_name())

def start_end_decorator(func):
  def wrapper(*args, **kwargs): # add args and kwargs so the function can have arguments
    print('Start')
    result = func(*args, **kwargs)
    print('End')
    return result
  return wrapper

@start_end_decorator
def add5(x):
  return x + 5

result = add5(10)
print(result)

import functools
def my_decorator(func):

  @functools.wraps(func) # preserves help info
  def wrapper(*args, **kwargs): # add args and kwargs so the function can have arguments
    # do...
    result = func(*args, **kwargs)
    # do...
    return result
  return wrapper

@my_decorator
def add5(x):
  return x + 5

#print(help(add5))
print(add5.__name__)

# decorators with arguments
def repeat(num_times):
  def decorator_repeat(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      for _ in range(num_times):
        result = func(*args, **kwargs)
      return result
    return wrapper
  return decorator_repeat

@repeat(num_times=3)
def greet(name):
  print(f'Hello {name}')

greet('Alex')

# nested decorators are executed in the order they are listed
# so the second decorator function runs inside the first decorator function
# debug decorator is a good idea
# timer decorator
# check behavior decorator
# plugins
# caches

# class decorators
# used if we want to maintain and update a state
class CountCalls:
  def __init__(self, func):
    self.func = func
    self.num_calls = 0

  def __call__(self, *args, **kwargs):
    self.num_calls += 1
    print(f'This is executed {self.num_calls} times')
    return self.func(*args, **kwargs)


@CountCalls
def say_hello():
  print('Hello')

say_hello()
say_hello()


# Generators
# generate objects that can be iterated over
# generate only 1 at a time, when you ask for it (more efficient)
# raises a StopIteration if you go past its yield count
def mygenerator():
  yield 1
  yield 2
  yield 3

g = mygenerator()

for i in range(2):
  print(next(g)) # next prints the next yield

a = mygenerator()
print(sum(a)) # 6
b = mygenerator()
print(sorted(b))

def countdown(num):
  print('Starting')
  while num > 0:
    yield num
    num -= 1

cd = countdown(4)
print(next(cd))
print(next(cd)) # remembers to start at the yield/while

import sys
def firstn(n):
  nums = []
  num = 0
  while num < n:
    nums.append(num)
    num += 1
  return nums

def firstn_generator(n):
  num = 0
  while num < n:
    yield num
    num += 1

print(sys.getsizeof(firstn(100000)))
print(sys.getsizeof(firstn_generator(100000)))
# don't need to save all the numbers in an array
# don't need to wait for all the elements to be generated before we start using them

# fibonacci example
def fibonacci(limit):
  a, b = 0, 1
  while a < limit:
    yield a
    a, b = b, a + b

fib = fibonacci(30)
for i in fib:
  print(i)

# generator expressions
# like list comprehensions but with ()
mygenerator = (i for i in range(100000) if i % 2 == 0)
  # all even elements from 0 to 9 in a generator object
print(sys.getsizeof(mygenerator)) # much smaller, saves memory

# vs list comprehension
mylist = [i for i in range(100000) if i % 2 == 0]
print(sys.getsizeof(mylist))


# Threads and Multiprocessing

# Process: an instance of a program
  # take advantage of multiple CPUs and cores
  # separate memory space: memory not shared between process
  # great for CPU-bound processing
  # new process is started independently from other processes
  # easily interruptable/killable
  # one global interpreter lock (GIL) for each process

  # -Heavyweight
  # -Starting a process is slower than starting a thread
  # -More memory
  # -IPC (inter-process communication) is more complicated

# Thread: entity in a process, can be scheduled
# aka lightweight process
  # all threads within a process share the same memory
  # lightweight
  # starting a thread is faster than starting a process
  # great for I/O-bound (input output) tasks
    # i.e. talking to slow devices

  # -Threading limited by GIL: only one thread at a time
  # -No efect for CPU-bound tasks
  # -Not interruptable/killable
  # -Careful with race conditions (two or more threads want to modify the same variable at the same time)

# Global interpreter lock (GIL)
  # A lock that allows only one thread at a time to execute in Python
  # Needed in CPython because memory management is not thread safe
  # To avoid
    # -Use multiprocessing
    # -Use a different, free-threaded Python implementation (Jython, IronPython)
    # -Use Python as a wrapper for third-party libraries (C/C++) they call code in C -> numpy, scipy

# multiprocessing code in VSCode

# parameters are the variables in the function()
# arguments are the values passed into the parameters
  # i.e. print_name('Alex') => 'Alex' is the argument

def foo(a,b,c):
  print(a,b,c)

foo(1,2,3) # positional arguments
foo(c=3, a=1, b=2) # keyword arguments, order does not matter
foo(1, c=3, b=2)
# cannot use a positional argument after a keyword argument
# cannot reassign a positional with keyword after

# default arguments
def foo(a, b, c, d=4):
  print(a,b,c,d)
foo(1,3,3)
# default arguments must be at the end of your parameter list

def foo(a, b, *args, **kwargs):
  # one * means you can pass any number of positional arguments
  # two ** means you can pass any number of keyword arguments
  print(a, b)
  for arg in args: # *arg is a tuple
    print(arg) # prints to same line
  for key in kwargs: # **kwargs is a dict
    print(key, kwargs[key])

foo(1,2,3,4,5,six=6,seven=7)

# force keyword argument
def foo(a, b, *, c, d):
  print(a,b,c,d)
  # every parameter after the * must be a keyword argument
  # same with *args
foo(1,2,c=3,d=4)

# unpacking arguments
def foo(a,b,c):
  print(a,b,c)
my_list = [0,1,2] # tuple works too
foo(*my_list) # equivalent to foo(0,1,2)
my_dict = {'a':2,'b':3,'c':9} # keys must match parameter names
foo(**my_dict) 

# local vs global variables
def foo():
  x = number # pulling from the global number variable declared below
  print('number inside function:', x)

number = 0
foo()

def foo():
  global number
  number = 3
  x = number
  print('number inside function:', x)

number = 0
foo()

# reassignment
def foo(x):
  x = 5

var = 10 # var is integer - immutable
foo(var)
print(var) # still 10

def foo(a_list):
  # a_list = [200, 300] rebinds the reference to a local variable, stops interacting with global variable
    # related: a += ... will stick with global, a = a + ... will rebind
  a_list.append(4)
  a_list[0] = -100
  
mylist = [1,2,3] # will be modified
foo(my_list)


# Asterisk Operator *
power = 2 ** 4 # 16
zeros = [0] * 10 # list with 10 zeroes
zeroone = [0, 1] * 10 # works with tuples and strings too

# list unpacking
# my_list = [arg1_value, arg2_value]
# foo(*my_list)
# my_dict = {'arg1':1, 'arg2',1}
# foo(**my_dict)

# unpack list, tuple, set into single or multiple elements
numbers = [1,2,3,4,5,6]
*beginning, last = numbers
print(beginning) # [1,2,3,4,5] always a list
print(last) # 6
beginning, *last = numbers
beginning, *middle, secondlast, last = numbers

# merge iterables into a list
my_tuple = (1,2,3)
my_list = [4,5,6]
my_set = {7,8,9}
new_list = [*my_tuple, *my_list, *my_set]

dict_a = {'a':1, 'b':2}
dict_b = {'c':3, 'd':4}
new_dict = {**dict_a, **dict_b}


# Shallow vs Deep copying
org = 5
cpy = org # both variables point to the same location
org = 6
print(org, cpy) # different

org = [0,1,2]
cpy = org
# now, changes to either will affect the other

import copy

# shallow copy: one level deep, only references of nested child objects
# deep copy: full independent copy

org = [0,1,2]
cpy = copy.copy(org) # shallow
cpy = list(org) # shallow
cpy = org[:] # shallow

org = [[0,1], [0,2]]
cpy = copy.deepcopy(org) # deep

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Company:
  def __init__(self, boss, employee):
    self.boss = boss
    self.employee = employee
    
p1 = Person('Alex', 55)
p2 = Person('Joe', 27)
company = Company(p1, p2)
company_clone = copy.deepcopy(company) # need deep copy to make Persons independent


# Context Managers
with open('notes.txt', 'w') as file: # less 'responsible'
  file.write('some todoo...')

file = open('notes.txt', 'w') # more 'responsible'
try:
  file.write('some todoo...')
finally:
  file.close()

# context manager class
class ManagedFile:
  def __init__(self, filename):
    self.filename = filename
    print('init')

  def __enter__(self): # executed as soon as with
    print('enter')
    self.file = open(self.filename, 'w')
    return self.file

  def __exit__(self, exc_type, exc_value, exc_traceback):
    # automatically exits file after we leave
    if self.file:
      self.file.close()
    if exc_type is not None:
      print('exception has been handled')
    #print('exc:', exc_type, exc_value)
    print('exit')
    return True # stops the throwing of exception

with ManagedFile('notes.txt') as file:
  print('do some stuff')
  file.write('some todo')
  file.error_method() # still exits :)
print('continuing')

# context manager function
from contextlib import contextmanager

@contextmanager
def open_managed_file(filename):
  f = open(filename, 'w')
  try: # enter
    yield f # will allocate and try to yield resource
  finally: # exit
    # can also handle exceptions here
    f.close()

with open_managed_file('notes.txt') as f:
  f.write('function context manager')