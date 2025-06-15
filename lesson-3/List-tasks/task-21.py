lis = sorted(list(map(int, input().split())))

print(f'Second smallest: {lis[1]}' if len(lis) > 1 else 'list has only one element')