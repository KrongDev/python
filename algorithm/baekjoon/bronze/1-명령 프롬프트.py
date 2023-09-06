

T = int(input()) - 1

answer = list(input())
for _ in range(T):
    text = list(input())

    new = []
    for x,y in zip(answer, text):
        if x == y:
            new.append(x)
        else:
            new.append('?')
    answer = new
print(''.join(answer))