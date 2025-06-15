# dic = {'key' : value, ...} - when given example dictionary

dic = {}

num = int(input('Enter the number of items: '))

# when items is string
for _ in range(num):
    key, value = input().split()
    dic[key] = value

# or another way
'''
import ast

dic ast.literal_eval(input())
'''

values = list(dic.values())

def is_unique(x):
    return values.count(x) == 1

cnt = 0
for i in values:
    if is_unique(i):
        cnt += 1
print(cnt)