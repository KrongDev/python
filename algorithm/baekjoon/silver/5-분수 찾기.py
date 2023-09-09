

a = int(input())

line = 1
while a > line:
    a -= line
    line += 1

child = 1
parent = 1
if line%2 ==0:
    child = a
    parent = line - a +1
else:
    child = line - a + 1
    parent = a

print(f'{child}/{parent}')