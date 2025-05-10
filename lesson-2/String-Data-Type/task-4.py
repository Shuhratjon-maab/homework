s = input()

print(s, 'is', 'not' * (s != s[::-1]), 'palindrome!')