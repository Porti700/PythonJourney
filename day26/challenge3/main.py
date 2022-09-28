## open file1.txt 
import os

with open('file1.txt', 'r') as f1:
    file1 = f1.readlines()
    print(file1)
        
with open('file2.txt', 'r') as f2:
    file2 = f2.readlines()
    print(file2)  
    
same_numbers = [int(num) for num in file1 if num in file2]              
print(same_numbers)