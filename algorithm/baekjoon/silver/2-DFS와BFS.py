max, line_size, start = map(int, input().split())

dfs_answer = []
bfs_answer = [start]

data = dict()
# 데이터 셋팅
for i in range(line_size):
    a, b = map(int, input().split())
    if data.get(a) is None:
        data[a] = [b]
    else:
        data[a].append(b)

    if data.get(b) is None:
        data[b] = [a]
    else:
        data[b].append(a)

# sorting
for key in data.keys():
    data[key].sort()

# 테스트 데이터
# {1: [2,3,4], 2: [4], 3: [4]}

# 깊은 탐색
def DFS(value):
    if value in dfs_answer:
        return

    dfs_answer.append(value)

    if not data.get(value):
        return

    for v in data[value]:
        DFS(v)


DFS(start)
print(*dfs_answer)

def BFS(s):
    queue = [s]
    while queue:
        node = queue.pop(0)
        if data.get(node) is None:
            continue
        for n in data[node]:
            if n not in bfs_answer:
                bfs_answer.append(n)
                queue.extend(data[node])


BFS(start)
print(*bfs_answer)