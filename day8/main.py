# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
# def greet():
#     print("Hello")
#     name = input("What is your name? ")
#     print(name)
    
# greet()


# Create a function with a input string

## Importante: Parametro es el nombre que se le da a los datos que se pasan y argumento el valor real de los datos
##             en la siguuiente funcion el parametro es "Name" y el argumento es "Kevin"


def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How you been {name}?")
  
greet_with_name("Kevin") 


## Funcionts with more than one input


def greet_with(name, location):
    print(f"This is your name {name}")
    print(f"This is your location {location}")
    
# greet_with("Kevin", "Altavista")       

## Funcionts with keyword arguments
   
greet_with(location = "altavista", name= "Kevins") 