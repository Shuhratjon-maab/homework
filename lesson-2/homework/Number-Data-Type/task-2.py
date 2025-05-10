a, b, c = map(int, input().split())
print(f'{max(a, b, c)} | min: {min(a, b, c)}')

nums = list(map(int, input().split()))
print('max: {} | min: {}'.format(max(nums), min(nums)))

nums = sorted(list(map(int, input().split())))
print('max: {mx} | min: {mn}'.format(mx = nums[-1], mn = nums[0]))