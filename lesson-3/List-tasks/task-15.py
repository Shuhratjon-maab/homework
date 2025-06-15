lis = list(map(int, input().split()))
even_count = 0

for i in lis:
    even_count += (1 - i % 2)

print('evens:', even_count)