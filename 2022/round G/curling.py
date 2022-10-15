import math
def circle(x1, y1, x2, y2, r1, r2):
    d = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
    r = 0
    if(d <= r1 - r2) or (d <= r2 - r1) or (d < r1 + r2) or (d == r1 + r2):
        r += 1
    return r

T = int(input())
for t in range(T):
    rs, rh = map(int, input().split())
    r, j = 0, 0
    n = int(input())
    for i in range(n):
        x, y = map(int, input().split())
        r += circle(0, 0, x, y, rh, rs)

    m = int(input())
    for i in range(m):
        z, w = map(int, input().split())
        j += circle(0, 0, z, w, rh, rs)
    if j == max(r, j):
        j = j - r
        r = 0
    else:
        r = r - j
        j = 0
    print("Case #"+str(t+1)+":", r, j)

