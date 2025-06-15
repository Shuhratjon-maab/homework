t = tuple(input().split()) # given tuple

print(t[-2] if len(t) > 1 else "not enough")

ln = len(t)

print(["empty", "has only one", f"secone largest is {t[-2]}"][ln > 0 + ln > 1])

#empty has only one element