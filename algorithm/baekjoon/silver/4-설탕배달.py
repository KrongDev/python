
"""
안일한점 :

충분히 한번에 풀 수 있는 문제임에도 3으로만 나눠 해결되는 케이스를 간과했다.

이로써 문제를 얼마나 대강 읽는지 알 수 있었고
해당 문제를 고치기 위해 노력을 해야할 것 같다.
"""

a = int(input())

answer = 0
while a >= 0:
    if a%5 == 0:
        answer += a//5
        break
    a -= 3
    answer += 1

if a < 0:
    print(-1)
else:
    print(answer)