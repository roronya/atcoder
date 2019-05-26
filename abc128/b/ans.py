from operator import itemgetter
from sys import stdin

def cast(sp, i):
  return (sp[0], -int(sp[1]), i)

N = int(input())
SP = [cast(stdin.readline().rstrip().split(), i+1) for i in range(N)]
#ans = sorted(SP, key=itemgetter(1), reverse=True)
#ans = sorted(SP, key=lambda x: x[1], reverse=True)
#print(ans)
#ans = sorted(ans, key=lambda x: x[0])
ans = sorted(SP)
print(ans)
for x in ans:
  print(x[2])
