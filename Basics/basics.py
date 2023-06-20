name = "Beau"
print(isinstance(name, str))

joe = 2
joe **= 3
print(joe)

print(not True)

# OR: if x is false, then y; else x.
print(0 or 1) # 1
print(False or 'hey') # 'hey'
print(True or 'sus') # True
print([] or False) # 'False', [] is treated as false

# AND only evalutes the second argument if the first is true. So: if x is false, x; else y.
print(False and 'hey') # False
print(True and 'sus') # 'sus'

# bitwise operators
# & binary AND
# | binary OR
# ^ binary XOR
# ~ binary NOT
# << shift left operation
# >> shift right operation

# is - check for same object
# in - membership operator

# Ternary operator (one-line if else)
def is_adult(age):
  return True if age > 18 else False

# multi line string
print(""" sus


saf""")

# string functions
print("beau".upper() + "BEAU".lower())
print("bEAu person". title())
print("person".islower())
print("peson".isalpha())
print("435151".isdecimal())
print("yoink".split("o"))
print(" asdf asdf sd".strip())
print("joe".find("j"))
print("j" in "joe") # operator
print(len("lol"))

name = "Sus\"sy\nbaka" # escape character \" \n
print(name)

name = "asdfh"
print(name[-1])
print(name[1:3])
print(name[3:])

# booleans
# numbers are always true, except 0
# strings are always true, except empty string
# dicts/lists are false when empty
done = True
print(type(done) == bool)

# any, all
print(any([True, True, False]))
print(all([True, True, True]))

# complex nums
num1 = 2+3j
num2 = complex(2,3)
print(num2.real, num2.imag)

# more number stuff
print(round(abs(-5.5)))
print(round(5.49, 1)) # specify rounding

# enums - numus bounded to a certain value
from enum import Enum

class State(Enum):
  INACTIVE = 0
  ACTIVE = 1

print(State.ACTIVE.value)
print(list(State))
print(len(State))