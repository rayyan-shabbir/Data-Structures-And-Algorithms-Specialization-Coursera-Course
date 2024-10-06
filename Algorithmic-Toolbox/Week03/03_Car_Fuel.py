d = int(input())
m = int(input())
n = int(input())

stops = list(map(int, input().split(" ")))

flag = False
count = 0

rem = m - stops[0]

for s in range(len(stops)-1):
    if rem < (stops[s+1] - stops[s]):
        count += 1
        rem = m

    if rem >= (stops[s+1] - stops[s]):
        rem -= (stops[s+1] - stops[s])
    else:
        flag = True

if flag:
    count = -1
elif rem < (d - stops[-1]):
    count += 1
    rem = m

rem -= (d - stops[-1])
print(count)