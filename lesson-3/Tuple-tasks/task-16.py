tup = input().split()
lis = list(tup)
sorted_tup = tuple(sorted(lis))

print("sorted:",sorted_tup == tup)