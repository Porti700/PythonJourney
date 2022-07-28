# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs. 

# Then check for the number of times the letters in the word LOVE occurs. 

# Then combine these numbers to make a 2 digit number.



# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


lower_name1 = name1.lower()
lower_name2 = name2.lower()

# CONTAR TRUE

t_name = lower_name1.count('t') + lower_name2.count('t')
r_name = lower_name1.count('r') + lower_name2.count('r')
u_name = lower_name1.count('u') + lower_name2.count('u')
e_name = lower_name1.count('e') + lower_name2.count('e')

true_total = t_name + r_name + u_name + e_name


# CONTAR LOVE

l_name = lower_name1.count('l') + lower_name2.count('l')
o_name = lower_name1.count('o') + lower_name2.count('o')
v_name = lower_name1.count('v') + lower_name2.count('v')
e_name = lower_name1.count('e') + lower_name2.count('e')

love_total = l_name + o_name + v_name + e_name

# suma

total_match = int (str(true_total) + str(love_total))




if total_match < 10 or total_match > 90:
    print(f"Your score is {total_match}, you go together like coke and mentos.")
elif total_match > 40 and total_match < 50:
    print(f"Your score is {total_match}, you are alright together.")
else:
    print(f"Your score is {total_match}.")
