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
