ls = input().split()

if ls:
    print('First element:', ls[0])
else:
    print('List is empty!')

# alternative:

print('First element:', ls[0] if ls else 'List is empty!')