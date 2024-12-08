import json

student = {
    "name" : "rm muzammil",
    "age" : 19,
    "grade" : "A"
}

print(student["grade"])

student["city"] = "New York"

student["age"] = 20

del student["city"]

for key,value in student.items():
    print(f"{key} : ")

for key,value in student.items():
    print(f"{value}")

for key,value in student.items():
    print(f"{key} : {value}")

if "grade" in student:
    print("True")

count = 0
for key in student.items():
    count +=1
print(count)

dict1 = {'a': 1, 'b': 2}  
dict2 = {'c': 3, 'd': 4}  

merged_dict = dict1 | dict2
print(merged_dict)

tuples_list = [('name', 'Alice'), ('age', 25), ('city', 'Paris')]
tuple_dict = dict(tuples_list)
print(tuple_dict)

unsorted_dict = {'z': 1, 'a': 2, 'c': 3}
sorted_dict = {key:unsorted_dict[key] for key in sorted(unsorted_dict.keys())}
print(sorted_dict)

simple_dict = {'a': 1, 'b': 2, 'c': 3}
reversed_dict = {value:key for key, value in simple_dict.items()}
print(reversed_dict)


def check_identiclity(dict1,dict2):
    if dict1 == dict2:
        return f"The two dicts {dict1} and {dict2} are identical"
    else:
        return f"The two dicts {dict1} and {dict2} are not identical"
dict1 = {'a':1,'b':2,'c':3}
dict2 = {'a':1,'b':2,'c':3}
print(check_identiclity(dict1,dict2))

person = {
    "name": "john",
    "Age": 30,
    "Address": {
        "street": "123 Elm St",
        "City": "Boston"
    }
}
print(json.dumps(person,indent=4))

print(person['Address']['City'])

person['Address']['phone'] = "123-456-7890"
print(person)

del person['Address']
print(person)

text_string = "hello world hello python world"
words = text_string.split()
word_counter = {}
for word in words:
    word_counter[word] = word_counter.get(word,0) + 1

print(word_counter)

simple_dict = {'a': 10, 'b': 15, 'c': 7}
max_key = max(simple_dict, key=simple_dict.get)
print(max_key)

# 23. Create a dictionary to map numbers 1 to 5 to their squares (e.g., {1: 1, 2: 4, 3: 9, ...}).

squares = {x:x**2 for x in range(1,6)}
print(squares)

# 24. Write a Python program to remove duplicate values from the dictionary {'a': 10, 'b': 15, 'c': 10, 'd': 15}.

sample_dict = {'a':10, 'b':15, 'c':10, 'd':15}
unique_dict = {}
seen_dict = set()
for key,value in sample_dict.items():
    if value not in seen_dict:
        unique_dict[key] = value
        seen_dict.add(value)
print(unique_dict)

# 25. Write a Python function that accepts a dictionary and a key, and returns the value associated with the key. If the key doesn’t exist, return "Key not found".

def find_value(sample_dict,k):

    for key,value in sample_dict.items():
        if key == k:
            return value

sample_dict = {'a':10, 'b':15, 'c':20, 'd':35}
key = 'b'
print(find_value(sample_dict,key))

# 26. Given two dictionaries dict1 = {'a': 5, 'b': 10} and dict2 = {'a': 3, 'b': 7}, write a Python program to add the values of matching keys and print the result.

dict1 = {'a': 5, 'b': 10, 'c':15}
dict2 = {'a': 3, 'b': 7, 'd':45}

result = {key: dict1.get(key,0) + dict2.get(key,0) for key in dict1.keys() | dict2.keys()}
result = dict(sorted(result.items()))
print(result)

# 27. Write a Python program to create a dictionary where the keys are the first n positive integers, and the values are their cubes. Take n as user input. 

def create_dict(n):
    sample_dict = {}
    for num in range(1,n+1):
        cube = num**3
        sample_dict[num] = cube
    return sample_dict
# num = int(input("Enter the number"))
num = 5
print(create_dict(num))

# 28. Flatten the following nested dictionary into a single-level dictionary:

nested_dict = {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': 4}}  
flatten_dict = {}
for key,sub_dict in nested_dict.items():
    for sub_key,value in sub_dict.items():
        flatten_dict[f"{key}.{sub_key}"] = value
print(flatten_dict)

# 29. Write a Python program to split a dictionary into two based on whether the values are odd or even.

sample_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
even , odd = {},{}
for key,value in sample_dict.items():
    if value % 2 == 0:
        even[key] = value
    else:
        odd[key] = value
print(f"All even values dict is {even}  and odd values dict is {odd} ")

# 30. Create a dictionary comprehension to filter out all keys in {'a': 1, 'b': 2, 'c': 3, 'd': 4} where the value is less than 3.

sample_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filter_dict = {key: value for key,value in sample_dict.items() if value >= 3}

print(filter_dict)