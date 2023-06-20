# lists continued
mylist = ["yo", "hello"]
mylist.sort()
newlist = sorted(mylist)
mylist.reverse()
mylist.remove("yo")
mylist.clear()

mylist = [0] * 5 # [0, 0, 0, 0, 0]
mylist2 = [1, 2, 3]
print(mylist + mylist2)

# slicing a list
mylist = [1,2,3,4,5,6,7,8,9]
a = mylist[1:4]
print(a)
# step index (optional)
a = mylist[::2]
print(a)

# copies modify the original
copy = mylist
copy.remove(1)
print(mylist)

# independent copies
independent_copy = mylist.copy()
independent_copy = mylist[:]
independent_copy = list(mylist)

a = [2,3,3]
b = [i*i for i in a]
print(b)


# Tuples
# Ordered and immutable, allows duplicate elements
# More efficient to create and iterate over a tuple
# Less space required compared to a list
mytuple = (1,3,"Max")
mytuple = 1,3,"Max" # parentheses are optional
mytuple = ("Pog",) # need comma so it recognizes as tuple
mytuple = tuple([1,3,"Max"])

if "Max" in mytuple: print ("yes")

print(mytuple.count('Max'))
print(mytuple.index(3))
mylist = list(mytuple) # conversion to list
mytuple = tuple(mylist)

# unpacking tuple
a = "Max", 28, "Boston"
name, age, city = a
print(name, age, city)

b = (0,1,2,3,4)
i1, *i2, i3 = b
print(i1, i2, i3) # i2 = [1,2,3]


# Dictionary
# key value pair
# unordered, mutable
mydict = {"name": "Max", "age": 28, "city": "NYC"}
del mydict["name"]
try:
  print(mydict["name"])
except:
  print("Error")

for key in mydict.keys(): # keys method returns a list with all the keys
  print(key)

for key in mydict.values(): # values method returns a list with all the values
  print(key)

for key, value in mydict.items(): # keys method returns a list with all the keys
  print(key, value)

# copying dictionary
mydict_copy = mydict.copy()
mydict_copy = dict(mydict)

# merge dictionaries with update()
a = {"name":"Max", "age":28, "email":"max@xyz.com"}
b = dict(name="Mary", age=27, city="Boston")
a.update(b)
print(a)
# also: you can any immutable as a key, even a tuple


# SETS
# unordered, mutable, no duplicates
myset = {1,2,3,1}
print(myset)
myset = set([1,32,5,6])

myset = set("Hello")
print(myset)
print(len(myset)) # figures out how many unique characters are in your word

# empty set
myset = set()

# methods
myset.add(1)
myset.remove(1) # will throw error if not exist
myset.discard(1) # does not throw error if not exist
myset.add(5)
print(myset.pop()) # removes an arbitrary value

if 1 in myset:
  print('yes')

# union, intersection, difference
odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

u = odds.union(evens)
print(u)
u = odds | evens
print(u)

print(odds.intersection(evens))
print(odds & evens)

setA = {1,3,4}
setB = {1,2}
diff = setA.difference(setB)
diff = setA - setB
print(diff)

diff = setB.symmetric_difference(setA) # all numbers that are in A and B, but not both
print(diff)

setA.update(setB) # adds elements found in another set without duplication
print(setA) 
setA.intersection_update(setB) # only keeps numbers found in both sets
setA.difference_update(setA) # removes elements found in other set
setA.symmetric_difference_update(setB) # only keeps elements found in A and B, but not both

# subset and superset
setA.issubset(setB)
setA.issuperset(setB)
setA.isdisjoint(setB) # disjoint: no shared elements

# copying
setB = setA.copy()
setB = set(setA)

# frozen set
# immutable version of normal set
a = frozenset([1,2,3,4])


# Strings - immutable
mystring = """Hello \
World""" # should not make new line
print(mystring)

char = mystring[0]
substring = mystring[1:3]
print(substring)
substring = mystring[::2]
if "e" in mystring: print("yes")

print(mystring.find("e"))
print(mystring.find("lol")) # -1 means not found
print(mystring.count('o'))
print(mystring.replace('World', 'Joe Biden')) # makes new string

# split
my_string = "how are you doing"
my_list = mystring.split() # default argument is a space
print(my_list)
my_string = "how,are,you,doing"
my_list = mystring.split(",")
print(my_list)

# join
new_string = ''.join(my_list)
print(new_string)

# timer
from timeit import default_timer as timer
start = timer()

sum = 0
for i in range(100000):
  sum += i
  
stop = timer()
print(stop-start)

# formatting strings
var = "tom"
my_string = "the var is %s" % var
var = 3
my_string = "the var is %d" % var # d for decimal
var = 3.0001
my_string = "the var is %.2f" % var # 2 specifies number of decimal places

var2 = "pog" 
my_string = "the variable is {}".format(var)
my_string = "the variable is {:.2f} and {}".format(var, var2)

my_string = f"the variable is {var*2}" # f-string
print(my_string)


# Collections
# special container data types

# Counter
from collections import Counter
a = "aaaaabbbbcc"
my_counter = Counter(a)
print(my_counter) # returns dict of char counts
print(my_counter.keys())
print(my_counter.most_common(2)[0][0]) # 2 most common types, returns a list with tuples
print(list(my_counter.elements()))

# named tuple
from collections import namedtuple
Point = namedtuple('Point', 'x,y') # creates a class with fields x, y
pt = Point(1, -4)
print(pt) # Point(x=1, y=-4)
print(pt.x)

# Ordered Dict
from collections import OrderedDict
# python 3.7 includes this functionality
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
print(ordered_dict)

# default dict
# has a default value if the value hasn't been set
from collections import defaultdict
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['c']) # returns default value of int, which is 0

# deque
# doubled ended queue, can remove elements from both ends
from collections import deque
d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
d.popleft()
d.extendleft([4,5,6]) # adds them in reverse
d.rotate(1) # moves all elements one place to the right
d.rotate(-1)
print(d)


# Itertools
# handles iterators

# product
from itertools import product
a = [1, 2]
b = [3, 4]
prod = product(a,b, repeat=2) # [(1,3,1,4), etc]
prod = product(a,b) # [(1, 3), (1, 4), (2, 3), (2, 4)]
print(list(prod))

# permutations
from itertools import permutations
a = [1,2,3]
perm = permutations(a)
perm = permutations(a, 2)
print(list(perm))

# combinations
from itertools import combinations, combinations_with_replacement
a = [1,2,3,4]
comb = combinations(a, 2)
print(list(comb))
comb2 = combinations_with_replacement(a, 2)
print(list(comb2))

# accumulate
from itertools import accumulate
import operator
a = [1,2,3,4]
acc = accumulate(a)
print(list(acc)) # [1,3,6,10]
acc = accumulate(a, func=operator.mul)
print(list(acc)) # [1,2,6,24]
a = [1,2,5,3,4]
acc = accumulate(a, func=max)
print(list(acc)) # [1,2,5,5,5]

# groupby
from itertools import groupby

def smaller_than_3(x):
  return x < 3
  
a = [1,2,5,3,1,4]
a.sort()
group_obj = groupby(a, key=smaller_than_3) # splits the list into groups based on function
for key, value in group_obj:
  print(key, list(value))

# infinite iterators
from itertools import count, cycle, repeat
for i in count(10): # infinite loop starting from 10
  print(i)
  if i == 15:
    break

a = [1,2,3]
# for i in cycle(a):
#  print(i) # 123123123123123123123...

for i in repeat(10, 4):
  print(i) # prints 10 four times


# Lambda
# arguments: expression
add10 = lambda x: x + 10
print(add10(1))

multiply = lambda x,y: x*y

# sorted with lambda
points2D = [(1,2), (15,1), (5,-1), (10,4)]
points2D_sorted = sorted(points2D) # sorts by first element
points2D_sorted = sorted(points2D, key=lambda x: x[1]) # sorts by second element
points2D_sorted = sorted(points2D, key=lambda x: x[0]+x[1]) # sort by sum of elements

# map with lambda
# map(func, seq)
a = [1,3,4,5]
b = map(lambda x: x*2, a)
b = [x*2 for x in a] # list comprehension
print(list(b))

# filter
# filter(func, seq) returns all elements where function returns true
b = filter(lambda x: x%2==0, a)
b = [x for x in a if x%2==0] # list comprehension
print(list(b))

# reduce
# reduce(func, seq)
from functools import reduce
a = [1,2,3,4,5,6] # say we want the product of all elements
product_a = reduce(lambda x,y: x*y, a)
print(product_a)


# Exceptions
x = -5
# if x < 0:
#  raise Exception("x should be positive")
# assert(x>=0), 'x is not positive'
try:
  a = 5 / 0
except ZeroDivisionError as e:
  print(e)
else:
  print("we chillin")
finally:
  print("cleaning up")

# our own exceptions
class ValueTooHighError(Exception):
  pass

class ValueTooSmallError(Exception):
  def __init__(self, message, value):
    self.message = message
    self.value = value

def test_value(x):
  if x > 100:
    raise ValueTooHighError('value is too high')
  if x < 5:
    raise ValueTooSmallError('value is too small', x)

try:
  test_value(0)
except ValueTooHighError as e:
  print(e)
except ValueTooSmallError as e:
  print(e.message, e.value)


# Logging
import logging
logging.basicConfig(
  level=logging.DEBUG,
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
  datefmt='%m/%d/%Y %H:%M:%S'
) # check documentation for more info

# 5 levels
logging.debug('debug')
  # 06/18/2023 16:12:40 - root - DEBUG - debug
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')

# from helper.py
import helper
  # 06/18/2023 16:14:42 - helper - INFO - Hello from helper


# log handlers
logger = logging.getLogger(__name__)
# create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')
# level and format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)
logger.addHandler(stream_h)
logger.addHandler(file_h)
  # in file.log: __main__ - ERROR - this is an error

logger.warning('this is a warning')
logger.error('this is an error')

# can also use a separate file logging.conf to setup loggers more easily

# capture and stack traces
import traceback

try:
  a = [1,2,3]
  val = a[4]
except IndexError as e:
  logging.error(e, exc_info=True) # includes the Traceback stuff in the log message
  logging.error("The error is %s", traceback.format_exc())

# rotating file handlers
from logging.handlers import RotatingFileHandler
# handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
# rolls over at 2000 to a new log file

# timed rotating file handler
from logging.handlers import TimedRotatingFileHandler
# handler = TimedRotatingFileHandler('timed_test.log', when='m', interval=1, backupCount = 5)
# s (seconds), m, h, d, midnight, w0 (week)
# rolls over after a certain amount of time

# JSON format logging
# github python-json-logger


# JSON
# JavaScript Object Notation
# heavily used in web apps
import json
# converting to JSON: json.dumps() (encoding, serialization)
person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}
personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)

# write JSON to file
with open('person.json', 'w') as file:
  json.dump(person, file, indent=4, sort_keys=True)

# converting JSON to python (deserialization, decoding)
person = json.loads(personJSON)

with open('person.json', 'r') as file:
  person = json.load(file)

print(person)

# custom class needs special encoding
class User:
  def __init__(self, name, age):
    self.name = name
    self.age = age

user = User('Max', 27)

# custom encoding function
def encode_user(o):
  if isinstance(o, User):
    return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
  else:
    raise TypeError('Object of type User is not JSON serializable')

userJSON = json.dumps(user, default=encode_user)
print(userJSON)

# or just alter the JSONEncoder itself
from json import JSONEncoder
class UserEncoder(JSONEncoder):
  def default(self, o):
    if isinstance(o, User):
      return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    return JSONEncoder.default(self, o)

userJSON = UserEncoder().encode(user)
print(userJSON)

# decoding back to class, need custom decode method
def decode_user(dct):
  if User.__name__ in dct:
    return User(name=dct['name'], age=dct['age'])
  return dct

user = json.loads(userJSON, object_hook=decode_user)
print(user) # now it is a class