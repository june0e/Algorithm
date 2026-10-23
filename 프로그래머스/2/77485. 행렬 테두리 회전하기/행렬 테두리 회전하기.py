def solution(rows, columns, queries):
    graph = [[0] * columns for _ in range(rows)]

    num = 1
    for r in range(rows):
        for c in range(columns):
            graph[r][c] = num
            num += 1

    answer = []

    for x1, y1, x2, y2 in queries:
        # 시작 칸의 값을 따로 보관
        temp = graph[x1 - 1][y1 - 1]
        min_value = temp

        # 위쪽: 왼쪽 → 오른쪽
        for c in range(y1, y2):
            min_value = min(min_value, graph[x1 - 1][c])
            temp, graph[x1 - 1][c] = graph[x1 - 1][c], temp

        # 오른쪽: 위 → 아래
        for r in range(x1, x2 - 1):
            min_value = min(min_value, graph[r][y2 - 1])
            temp, graph[r][y2 - 1] = graph[r][y2 - 1], temp

        # 아래쪽: 오른쪽 → 왼쪽
        for c in range(y2 - 1, y1 - 1, -1):
            min_value = min(min_value, graph[x2 - 1][c])
            temp, graph[x2 - 1][c] = graph[x2 - 1][c], temp

        # 왼쪽: 아래 → 위
        for r in range(x2 - 1, x1 - 1, -1):
            min_value = min(min_value, graph[r][y1 - 1])
            temp, graph[r][y1 - 1] = graph[r][y1 - 1], temp

        # 마지막에 남은 값을 시작 칸에 넣기
        graph[x1 - 1][y1 - 1] = temp
        answer.append(min_value)

    return answer