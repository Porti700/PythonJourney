################### Scope ####################



## Local Scope

# def drink_portion():
#     potion_strength = 1
#     print(potion_strength)
    
# drink_portion() 
# print (potion_strength)    

## Global Scope

# from operator import ne


# player_health = 10

# def drink_portion():
#     potion_strength = 2
#     print(player_health) 
    
# ## There is no block scope

# game_level = 3
# def create_enemy():
#     enemies = ["Skeletons", "Zombie","Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]
#     print(new_enemy)     
             
       
## Modifying the Global scope
            
# enemies = 1

# def increase_enemies():
#     print(f"enemies inside function: {enemies}")
#     return enemies + 1

# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")      


## Global Constants, se usan solo en mayusculas. Just uppercase

PI = 3.14159
URL = "www.google.com"

      