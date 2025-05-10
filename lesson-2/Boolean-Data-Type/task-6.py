n = int(input())
if n % 3 == 0 and n % 5 == 0:
    pass

if n % 15 == 0:
    pass

print('It’s {}divisible by both 3 and 5.'.format('not ' * n % 15 != 0))