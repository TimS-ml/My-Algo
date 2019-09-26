import os, datetime
import matplotlib.pyplot as plt

base_dir = 'D:\\Python\\LeetCode_python'
# base_dir = 'home/jian/Documents/Python/LeetCode_python/'
file_list = os.listdir(base_dir)
# print(file_list)
date_m_list = {}
x = []
y = []

for i in range(0, len(file_list)):
    path = os.path.join(base_dir, file_list[i])
    if os.path.isdir(path):
        continue
    timestamp1 = os.path.getmtime(path)  # 修改时间
    # timestamp2 = os.path.getctime(path)  # 创建时间

    date_m = datetime.datetime.fromtimestamp(timestamp1)
    # date_c = datetime.datetime.fromtimestamp(timestamp2)
    
    # print(file_list[i], '修改时间:', date_m.strftime('%Y-%m-%d %H:%M:%S'))
    # print(file_list[i], '修改时间:', date_m.strftime('%Y-%m-%d'))
    
    n = date_m.strftime('%m-%d')

    if n in date_m_list:
        date_m_list[n] += 1
    else:
        date_m_list[n] = 1

for i in sorted (date_m_list) : 
    # print((i, date_m_list[i]), end =" ") 
    x.append(i)
    y.append(date_m_list[i])

# x, y = date_m_list.keys(), date_m_list.values()
print(x, y)

plt.bar(x, y)
plt.xticks(rotation = 45)
plt.show()
