ls = input().split()

if ls:
    print('Last element:', ls[-1])
else:
    print('List is empty!')

# alternative:

print('Last element:', ls[0] if ls else 'List is empty!')