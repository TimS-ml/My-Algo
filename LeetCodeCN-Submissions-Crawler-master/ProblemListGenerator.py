# 对应的读取文件格式请参考同文件夹下的 1.txt 文件
dic = {}
with open("1.txt", "r") as f:
    ff = f.readlines()
    for line in ff:

        print(line.split("\t"))
        num, title = line.split("\t")
        title = title[:-1]
        dic[title] = int(num)
print(dic)
