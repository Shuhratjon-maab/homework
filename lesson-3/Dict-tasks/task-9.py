dic = {'a' : 1}


if not dic:
    print('empty') # not empty

dic.clear()

if not dic:
    print('empty') # empty

# or anothe way
bool(dic)