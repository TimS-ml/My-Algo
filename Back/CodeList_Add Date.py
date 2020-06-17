import os
# import pandas as pd
# import numpy as np
# import warnings
# warnings.simplefilter(action='ignore', category=FutureWarning)
# import calendar

# dict = {}
# months = [(calendar.month_abbr[i]) for i in range(1, 13)]
# print(months)


# open file README.md
PATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))
os.chdir(PATH)
file = open('CodeList.md', mode='a', encoding='utf-8')

startdate = 186
for i in range(60):
    content = '## Day ' + str(startdate) + '\n\n\n\n'
    file.write(content)
    startdate += 1

print('Done!')
