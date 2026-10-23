from collections import deque

def solution(maps):
    rows = len(maps)
    cols = len(maps[0])

    # S, L, E의 위치 찾기
    positions = {}
    for r in range(rows):
        for c in range(cols):
            if maps[r][c] in "SLE":
                positions[maps[r][c]] = (r, c)

    def bfs(start, target):
        q = deque([(start[0], start[1], 0)])
        visited = [[False] * cols for _ in range(rows)]
        visited[start[0]][start[1]] = True

        # 행 변화량, 열 변화량: 아래, 위, 왼쪽, 오른쪽
        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]

        while q:
            x, y, distance = q.popleft()

            if (x, y) == target:
                return distance

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if (0 <= nx < rows and 0 <= ny < cols
                    and maps[nx][ny] != "X"
                    and not visited[nx][ny]):

                    visited[nx][ny] = True
                    q.append((nx, ny, distance + 1))

        return -1

    # 시작점 → 레버
    to_lever = bfs(positions["S"], positions["L"])
    if to_lever == -1:
        return -1

    # 레버 → 출구
    to_exit = bfs(positions["L"], positions["E"])
    if to_exit == -1:
        return -1

    return to_lever + to_exit