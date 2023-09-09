"""
아무리 생각해도 궁금하다 등차 수열이 연속된 두자리의 차가 같을경우라는데
그럼 101, 202도 포함이 아닌가...?

수학공부도 화이팅...!
코드로 구현하기 자체는 쉬웠는데 저 개념이 이해가 잘 안되긴 한다
"""

def check(num):
    if 0 < num < 100:
        return True
    c = [*map(int, str(num))]

    if c[0] - c[1] == c[1] - c[2]:
        return True

    return False


a = int(input())

answer = 0
for n in range(1, a + 1):
    if check(n):
        answer += 1

print(answer)
