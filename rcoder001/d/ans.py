N = input()
t = list(map(int, input().split()))
v = list(map(int, input().split()))
t.append(-1)
v.append(-1)
#print(N, t, v)

sign = "+"
ans = 0.0
turn = 0
current_speed_limit = v[0]
next_speed_limit = v[1]
current_time_limit = t[0]
current_speed = 0
memo_time = 0
for current_time in range(sum(t)):
  print(ans)
  if next_speed_limit == -1: #次のターンが無い
    if current_speed == current_time_limit - current_time: # 減少になったとき全部計算して終わり
      if sign == "=":
        ans += current_speed * (current_time - memo_time)
      if sign == "+":
        ans += current_speed * (current_time - memo_time)/2
      ans += current_speed * (current_time_limit*current_time)/2
      break
    if current_speed == current_speed_limit:
      if sign == "+":
        ans += current_speed * (current_time - memo_time)/2
        memo_time = current_speed
        sign = "="
    else:
      current_speed += 1
print(ans)
