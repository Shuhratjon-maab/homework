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

value = input()
keys_for_value = []

for i in dic.keys():
    if dic[i] == value:
        keys_for_value.append(i)

if keys_for_value:
    print(f"The keys for the value:\n{keys_for_value}")
else:
    print("The value doesn't exist!")