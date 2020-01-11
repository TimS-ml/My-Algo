import os
import numpy as np
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


# open file README.md
PATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))
os.chdir(PATH)
file = open('README.md', mode='r', encoding='utf-8')

# columns = ["Day", "Q", "Dif", "St"]
question = np.empty((0, 4))  # 0 => len(row)=0
finish = np.empty(0)
q_count = np.empty((0, 2))  # Day count, days without leetcode

# py file in dir
for pyfile in os.listdir("../LC-py"):
    # or use if np.any(finish[:] == pyfile.split('-')[0]) == False
    # np.in1d(pyfile.split('-')[0], finish) == False is compare list to list, quite slow
    if pyfile.split('-')[0] not in finish and 2 < len(pyfile.split('-')[0]) < 5 and pyfile.split('.')[-1] == 'py':
        finish = np.append(finish, np.array([pyfile.split('-')[0]]), axis=0)
# print(finish)

temp = '00'
Day = '00'
count = 0
for line in file:
    if 'Day' in line:
        Day = line.split(' ')[2]
        Day = Day.split('\n')[0]

    if temp != Day:
        q_count = np.append(q_count, np.array([[temp, count]]), axis=0)
        temp = Day
        count = 0

    if ' = ' in line:
        Q = line.split(' ')[0][1:]  # Question
        D = line[0]  # Difficulty
        # the question should be finish or pending if has '='
        # one question may show up multiple times when rev
        S = line.split(' = ')[1]  # state
        S = S.split('\n')[0]
        count += 1

    elif line[0] == 'E' or line[0] == 'M' or line[0] == 'H':
        Q = line.split(' ')[0][1:]
        Q = Q.split('\n')[0]
        D = line[0]
        S = 'Y'
        count += 1

    else:
        continue

    # if Q not in finish and len(S) == 1:
    # if np.where(dates_list==date_now, True, False) and len(S) == 1:
    if Q not in finish[:] and len(S) == 1:
        S = 'N'

    question = np.append(question, np.array([[Day, Q, D, S]]), axis=0)


undo = q_count[np.where(q_count[:, -1] == '0')]
print(undo)
print(undo.shape)
# print(question[np.where(question[:, -1] == 'N')])
# print(np.setdiff1d(finish, question[:, 1]))
