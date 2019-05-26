N = int(input())
a = []
for i in range(N):
    N, K = input().split()
    K = int(K)
    a.append([N, -K, i+1])
a.sort()
for a_ in a:
    print(a_[2])
