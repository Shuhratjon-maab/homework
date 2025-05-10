un = input()
ps = input()
if un and ps:
    print('Both are not empty')
elif ps:
    print('Username is empty.')
elif un:
    print('Password is empty.')
else:
    print('Both are empty')
