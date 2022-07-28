## Write a function that takes a character and returns True if it is a vowel, otherwise returns False
import re


def vowel(character):
    """AI is creating summary for vowel

    Args:
        character (vowel): [description]

    Returns:
        True: [description]
    """
    
    if character == "a" or "e" or "i" or "o" or "u":
        return True
    else:   
        return False
    
print(vowel("3"))    