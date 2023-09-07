"""
내가 알지 못했던 혹은 구현은 하였지만 타임 아웃 뜬 것듯 그리고 공식으로 외워야하는 것들 을 정리 해놓는 곳

생각 못했다면 자존심이 많이 상하지만 그래도 힘내서 해보자
"""


"""
dfs를 사용한 경우의 수 출력
6개씩 그룹지어 경우의 수를 체크
수 자리는 오름차순 정렬
"""
def dfs(depth, idx):
    if depth == 6:
        print(*out)
        return

    for i in range(idx, k):
        out.append(s[i])
        dfs(depth + 1, i + 1)
        out.pop()


while True:
    a = list(map(int, input().split()))
    k = a[0]
    s = a[1:]
    out = []
    dfs(0, 0)
    if k == 0:
        exit()
    print()
