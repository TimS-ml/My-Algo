# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.append.html
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.count.html


import os
import pandas as pd
# import pprint


# open file README.md
PATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))

os.chdir(PATH)
file = open('README.md', mode='r', encoding='utf-8')

# py file in dir
finish = []
for pyfile in os.listdir(PATH):
    if pyfile.split('-')[0] not in finish and 2 < len(pyfile.split('-')[0]) < 5 and pyfile.split('.')[-1] == 'py':
        finish.append(pyfile.split('-')[0])
# print(finish)

# buile data frame
question = pd.DataFrame(columns = ["Day", "Q", "D", "St"])
for line in file:
    if 'Day' in line:
        Day = line.split(' ')[2]
        Day = Day.split('\n')[0]

    if 'pending' in line:
        Q = line.split(' ')[0][1:]
        D = line[0]
        S = 'P'
    elif line[0] == 'E' or line[0] == 'M' or line[0] == 'H':
        Q = line.split(' ')[0][1:]
        Q = Q.split('\n')[0]
        D = line[0]
        S = 'Y'
    else:
        continue

    if Q not in finish and S != 'P':
        S = 'N'

    question = question.append({
        'Day': Day, 
        'Q': Q, 
        'D': D,
        'St': S}, ignore_index=True)
# print(question.describe())

print(question['St'].value_counts())
print(question.loc[question.St == 'N'])
# print(question.loc[question.St == 'P'])

df = question.loc[question.St == 'N']
df.to_csv('000_Undo.txt', index=None, sep=' ', mode='a')
print('Done!')
