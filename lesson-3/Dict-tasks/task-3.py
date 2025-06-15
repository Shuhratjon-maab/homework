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

number_of_keys = len(dic.keys())

print('The number of keys:', number_of_keys)