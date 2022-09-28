#  List comprehension
# Append list normal way

# numbers = [1,2,3,4]
# new_list = []
# for i in numbers:
#     add= i +1
#     new_list.append(add)
# print(new_list)

# Append using list comprehension
numbers = [1,2,3,4]
new_list = [n+1 for n in numbers]
# print(new_list)
# new_list = [new_item for item in list]

# Create a variable called "Angela"

name = "Angela"
x = name.split()
# print(x)
letter_list = [letter for letter in name]
# print(letter_list)

# Crate a new list using range

range_list = [n*2 for n in range(1,5)]
# print(range_list)


names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) > 5]
# upper_names = [n.capitalize for n in long_names]

print(long_names)