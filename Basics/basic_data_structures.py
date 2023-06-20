dogs = ["Beau", 2, False]
dogs += ["Bob"]
dogs.append(3)
print("Beau" in dogs)

# pop returns and removes the last item
print(dogs.pop())
print(dogs)

# adding at the middle
dogs.insert(2, "Test")
print(dogs)

# slice
dogs[1:1] = ["Test1", "Test2"]
print(dogs)

# sort and copy
items = ["aasdf", "b", "a"]
itemscopy = items[:]
items.sort(key=str.lower)
print(items)
print(itemscopy)

# sort without editing original list
items2 = ["b", "asd", "s"]
print(sorted(items2, key=str.lower))
print(items2)


# tuples - cannot be modified
names = ("Roger", "Syd", "Beau")
names.index("Roger")
print(len(names))
print("Roger" in names)
print(names[0:2])
print(sorted(names))
newTuple = names + ("Tina", "a")

# dictionaries - key value pairs
dog = { "name": "Roger", "age": 8, "asdf": 0, "s": 5 }
dog["name"] = "joe"
print(dog["name"])
print(dog.get("name"))
print(dog.get("color", "brown")) # brown is default
print(dog.popitem()) # takes out last item and returns it
print(list(dog.keys()))
print(dog.pop("asdf"))
print(list(dog.items()))
print(len(dog))
del dog['age']

# Sets - unordered, like mathematical sets
set1 = {"Roger", "Syd", "Roger"}
set2 = {"Roger"}
# cannot have two of the same item
intersect = set1 & set2
union = set1 | set2
difference = set1 - set2
does1include2 = set1 > set2
print(list(set1))

# Functions
def hello(age, name="my friend"): # optinal argument that defaults to "my friend"
    print(name)

# mutable objects can be changed by functions
def change(value):
  value["name"] = "sus"
sadf = {"name": "joe"}
change(sadf)
print(sadf)

# nested functions - inner function scope is the outer function
def count():
  count = 0
  def increment(): 
    nonlocal count # use global count
    count += 1
    print(count)
  increment()
count()