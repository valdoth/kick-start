t = int(input())
for i in range(t):
    m, n, p = map(int,input().split())
    tab = [ [0]*m for i in range(n)]
    for j in range(m):
        temp = list(map(int, input().split()))
        for k in range(n):
            tab[k][j] = temp[k]
    r = 0
    #print(tab, p, m, n)
    for y in tab:
        if y[p-1] != max(y):
            r += max(y) - y[p-1]
        #print("test",y)
    print("Case #"+str(i+1)+":", r)
