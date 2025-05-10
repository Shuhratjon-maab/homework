a = input()
b = input()

print (f'{a} {"don't" * (a not in b)} contains {b}')