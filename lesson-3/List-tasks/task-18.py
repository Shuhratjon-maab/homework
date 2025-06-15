lis = input().split()
sub_lis = input().split()

check = False
k = 0
for i in lis:
    if i == sub_lis[k]:
        k += 1
        if k + 1 == len(sub_lis):
            check = True
            break
    else:
        k = 0
    # k = (k + 1) * (i == sub_lis[k])
    # if k + 1 == len(sub_lis):
    #    check = True
    #    break

print('Sublist is in list:', check)


lis = input()
sub_lis = input()

check = sub_lis in lis

print('Sublist is in list:', check)

# print(f"Sublist {["isn't"]['is'][sub_lis in lis]} in the list.")