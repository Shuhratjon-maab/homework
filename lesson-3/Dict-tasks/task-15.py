keys = input().split()
values = input().split()
dic = {}

for i in range(len(keys)):
    dic[keys[i]] = values[i]

print(dic)