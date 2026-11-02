# Hashsets
s = set()

# Add item into Set - O(1)
s.add(1)
s.add(2)
s.add(3)

print(s)
# Lookup if item in set - O(1)
if 1 in s:
    print(True)

s.remove(3)

print(s)


string = 'aaaaaaaabbbbbbbbbbccccccccccc'
sett = set(string)

print(sett)

# O(n)
for x in s:
    print(x)

# Hashmaps - Dictionaries

d = {'greg': 1, 'steve': 2, 'rob': 3}

print(d)

# Add key: val in dict: O(1)
d['arsh'] = 4

print(d)

# Check for presence of key in the dict: O(1)
if 'greg' in d:
    print(True)

# Check the value corresponding to a key in the dict: O(1)
print(d['greg'])

# Loop over the key: val pairs of the dictionary: O(n)
for key, val in d.items():
    print(f'key {key}: val {val}')

# Defaultdict
from collections import Defaultdict

default = Defaultdict(int)
default[2]

print(default)


# Counter
from collections import Counter

counter = Counter(string)
print(counter)