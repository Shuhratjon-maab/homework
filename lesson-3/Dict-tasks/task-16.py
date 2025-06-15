# dic = {'key' : value, ...} - when given example dictionary

dic = {}

import ast

dic = ast.literal_eval(input())

ans = "Dict type doesn't exist in values!"
for value in dic.values():
    if type(value) == dict:
        ans = "Dict type does exist in values!"
        break

print(ans)