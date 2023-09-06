num = int(input())
datas = list(map(int, input().split()))
maxNum = max(datas)

answer = 0
for data in datas:
    answer += (data/maxNum * 100)

print(answer/num)
