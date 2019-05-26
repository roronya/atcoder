N = int(input())
rs = []
for no in range(N):
    S, P = [i for i in input().split()]
    rs.append((S, int(P), no+1))
rs = sorted(rs, key=lambda x: x[1], reverse=True)
rs = sorted(rs, key=lambda x: x[0])
for r in rs:
    print(r[2])
