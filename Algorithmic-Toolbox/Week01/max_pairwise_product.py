n = int(input())

lst = list(map(int, input().split(" ")))

max1_ind = 0
for i in range(1, n):
    if lst[i] > lst[max1_ind]:
        max1_ind = i


max2_ind = -1

for i in range(n):
    if i != max1_ind:
        if max2_ind == -1 or lst[i] > lst[max2_ind]:
            max2_ind = i

print(lst[max1_ind]*lst[max2_ind])

    