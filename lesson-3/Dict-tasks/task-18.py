from collections import defaultdict

def default():
    return 'Default'

dic = defaultdict(default)

print(dic['missing_key'])