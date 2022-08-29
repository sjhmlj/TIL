while True:
    w, h = map(int, input().split())
    dx = [-1, 0, 1, 1, -1, 0, 1, -1]
    dy = [1, 1, 1, 0, 0, -1, -1, -1]
    if (w == 0) and (h == 0):
        break
    check = [[False] * w for _ in range(h)]
    island = [list(map(int, input().split())) for _ in range(h)]
    stack = []
    cnt = 0
    for x in range(h):
        for y in range(w):
            if island[x][y] == 1:
                if check[x][y] == False:
                    cnt += 1
                stack.append((x, y))
                while len(stack) != 0:
                    cur = stack.pop()
                    if (island[cur[0]][cur[1]] == 1) and (check[cur[0]][cur[1]] == False):
                        check[cur[0]][cur[1]] = True
                        for a in range(8):
                            mx = cur[0] + dx[a]
                            my = cur[1] + dy[a]
                            if (0 <= mx < h) and (0 <= my < w) and (check[mx][my] == False) and (island[mx][my] == 1):
                                stack.append((mx, my))
    print(cnt)