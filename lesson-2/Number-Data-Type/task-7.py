num = int(input())

print('Number is', end = '')
print('odd' if num % 2 else 'even')

print('Number is', ['even', 'odd'][num % 2])