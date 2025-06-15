org_list = input().split()
new_list = sorted(org_list)

print('The sorted list:', *new_list)

# if it's about numbers:

org_list = list(map(int, input().split()))
new_list = sorted(org_list)

print('The sorted list:', *new_list)
