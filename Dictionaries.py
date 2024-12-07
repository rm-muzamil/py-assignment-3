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