##Create a new class
## Cada nombre de clase la  primera letra siemre es mayuscula.
## EL nombre de la clase se llama User.

class User:
    ## Creamos el constructor init para inicializar la clase
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        
    ## Creamos un metodo llamado Follow
    def Follow(self, user):
        user.followers += 1
        self.following += 1

## EL nombre del objeto se llama User_1
user_1 = User("001", "kevin")    
user_2 = User("002", "ernesto")
print(user_1.username)

user_1.Follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

## Atributos que se le da al objeto User_1 son ID y Name
## Atributos son variables que estan asociadas a un objeto

# user_1.id = "001"
# user_1.name = "John"


