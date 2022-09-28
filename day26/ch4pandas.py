import pandas

student_dict = {
"student": ["Angela", "James", "Lily"],
"score": [56, 76, 98]
}
 
#  Looping through dictionaries.
# for (key, value) in student_dict.items():
#     print (key)
    
students_data_frame = pandas.DataFrame(student_dict)
# print (students_data_frame)    
    
#  Loop through dataframe in pandas

# for (key, value) in students_data_frame.items():
#     print (value)
    
# Loop through rows of a  dataframe 

for (index, row) in students_data_frame.iterrows():
    print (index.student)