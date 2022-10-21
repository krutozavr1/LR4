a, b = int(input()), int(input())
c = max(abs(a), abs(b))
d = min(abs(a), abs(b))
print(c % d + 1)
