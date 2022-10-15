n = int(input())
for i in range(n):
    m = int(input())
    k = list(map(int, input().split()))
    r = 0
    for j in range(m):
        for l in range(j,m):
            if k[j:l+1][0] >= 0 and sum(k[j:l+1]) >= 0:
                #print(k[j:l+1])
                r += sum(k[j:l+1])
            elif 0 > sum(k[j:l+1]):
                break
    print("Case #" + str(i+1) + ": " + str(r))
