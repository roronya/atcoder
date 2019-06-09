N = int(input())
K = int(input())

old = [1]
for i in range(N):
  new = []
  for i in old:
    new.append(i*2)
    new.append(i+K)
  old = new
print(min(old))
