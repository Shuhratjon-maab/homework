sum_of = sum(map(int, input.split()))
print(['smaller than 50', 'equal to 50', 'greater than 50'][(sum_of > 50) + (sum_of >= 50)])