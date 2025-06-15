lis = sorted(list(map(int, input().split())))

print(f'Second largest: {lis[-2]}' if len(lis) > 1 else 'list has only one element')