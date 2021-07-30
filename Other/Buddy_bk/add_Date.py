import datetime

file = open('./Tim.md', mode='a', encoding='utf-8')

date1 = '20210614'  # [prev + 12] last stage end date + 1

start = datetime.datetime.strptime(date1, '%Y%m%d')
step = datetime.timedelta(days=1)
peroid = 12


# Repo `buddy`

budContent = '''
Time of Study: xxx+xxx+xxx min
- [-] Goal
  - [ ] Info Gathering + Self-promo
  - [ ] Paper
  - [ ] Book
  - [ ] Algorithm
- [-] Exercise
  - [ ] Jogging
  - [ ] Workout
- [-] Working
  - [ ] Math
  - [ ] Project
Random thoughts:

[Based on rt1 v12.27]

'''

start = datetime.datetime.strptime(date1, '%Y%m%d')
for count in range(peroid):
    content = '## ' + start.strftime('%Y%m%d')
    content += budContent
    file.write(content)
    start += step
