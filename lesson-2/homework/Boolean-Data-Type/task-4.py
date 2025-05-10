a, b, c = map(int, input().split())

if a == b or b == c or a == c:
    print('Number are not different.')
else:
    print('Number are different.')

if a != b and b != c:
    print('Number are different.')
else:
    print('Number are not different.')

print('Numbers are', 'not' * (len(set([a, b, c])) != 3), 'different.')