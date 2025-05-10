n = int(input())

check = ' not' * (n % 2 != 0 or n <= 0)
print(f'{n} is{check} positive and even.')