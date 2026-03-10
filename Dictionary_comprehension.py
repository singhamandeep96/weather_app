names= ['ALex', 'Beth','Caroline','Dave','Eleanor','Freddie']

import random

student_scores={student:random.randint(1,100) for student in names}

print(student_scores)

passed_students={student:score for (student, score) in student_scores.items() if score > 60 }
print(passed_students)



import pandas as pd

student_dict= {
    "student": ["Angela", "James", "Lily"],
    "score": [56,76,98]
}
student_data_frame= pd.DataFrame(student_dict)
print(student_data_frame)

## Loop through data frame
for (key, value) in student_data_frame.items():
    print(value)

##Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row.student)