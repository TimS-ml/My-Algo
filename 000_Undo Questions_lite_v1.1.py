import os


# open file README.md
os.chdir("../LC-py")
file = open('README.md', mode='r', encoding='utf-8')

question = {'E':[], 'M':[], 'H':[], 'P':[]}
finish = []
unfinish = []

for line in file:
    if ' = ' in line:
        question['P'].append(line.split(' ')[0][1:])
    elif line[0] == 'E':
        question['E'].append(line.split('\n')[0][1:])
    elif line[0] == 'M':
        question['M'].append(line.split('\n')[0][1:])
    elif line[0] == 'H':
        question['H'].append(line.split('\n')[0][1:])
# print(question)

# py file in dir
for pyfile in os.listdir("../LC-py"):
    if pyfile.split('-')[0] not in finish and 2 < len(pyfile.split('-')[0]) < 5 and pyfile.split('.')[-1] == 'py':
        finish.append(pyfile.split('-')[0])

# find undo questions
for key, q_list in question.items():
    for i in q_list:
        if i not in finish:
            print(key, i)
