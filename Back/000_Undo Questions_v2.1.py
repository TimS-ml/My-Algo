# update Mark question


import os
import pandas as pd
import numpy as np


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
question = pd.DataFrame(columns=["Day", "Q", "Dif", "St"])
for line in file:
    if 'Day' in line:
        Day = line.split(' ')[2]
        Day = Day.split('\n')[0]

    if ' = ' in line:
        Q = line.split(' ')[0][1:]
        D = line[0]
        # the question should be finish or pending if has '='
        # one question may show up multiple times when rev
        S = line.split(' = ')[1]
        S = S.split('\n')[0]

    elif line[0] == 'E' or line[0] == 'M' or line[0] == 'H':
        Q = line.split(' ')[0][1:]
        Q = Q.split('\n')[0]
        D = line[0]
        S = 'Y'

    else:
        continue

    if Q not in finish and len(S) == 1:
        S = 'N'

    question = question.append({
        'Day': Day,
        'Q': Q,
        'Dif': D,
        'St': S}, ignore_index=True)
# print(question.describe())
# print(question)
# print(question['St'].value_counts())
print(question.loc[question.St == 'N'])
# print(question[(question.St!="Y")&(question.St!="N")])


# output to txt
def output_txt(question, out):
    if out == -1:
        return
    df = question.loc[question.St == 'N']
    df.to_csv('000_Undo.txt', index=None, sep=' ', mode='a')
    print('Done!')


out = -1
output_txt(question, out)
