# Asterisk is the key in this class, because with the asterisk i have unlimited arguments
# (*args)

# def add(*args):
#     for i in args:
#         print(i)
        
        
# Challenge: Create a function that sums an unlimited numbers of arguments.

def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(5,65,3))


# ** Kwargs for keyword arguments.

def calculate(**kwargs):
    # print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
        
    
        
calculate(add = 1, multiply = 5)   


# todo: create a function that returns the same word inverted 

def word(self):
    name = input("word: ")
    '''docstring'''    
    
    


