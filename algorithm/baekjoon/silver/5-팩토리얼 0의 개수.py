from functools import reduce

a = int(input())
b = 1
for n in range(a):
    b = b* (n + 1)
c = str(b)
d = reduce(lambda x,y: y + x, c)

count = 0
for num in d:
    if num != '0':
        break
    count += 1


print(count)
