import pandas as pd
import numpy as np


# Question 1
# For creating series object in pandas we can use only one-dimensiaonal arrays (vectors)


# Question 2
data = [1,2,3,4,5,6,7,8,9,10,11,12]
df = pd.Series(data, index=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

print(df)


# Question 3
data = [35, 36, 39, 42]
df = pd.Series(data, index=['MatMIE', 'MatDAIS', 'COMIE', 'COMEC'])

print(df)


# Question 4
exam_data = {
	'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
	'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)

print(df)


# Question 5
attempts = df['attempts'] > 2
print(df.loc[attempts])