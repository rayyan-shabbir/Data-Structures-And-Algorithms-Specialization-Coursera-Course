n, W = map(int, input().split(" "))

c = []
w = []
v = []
amount = 0

for i in range(n):
    c_temp, w_temp = map(int, input().split(" "))
    c.append(c_temp)
    w.append(w_temp)

# print(W)
# print(n)
# print(c)
# print(w)

for i in range(n):
    v.append(c[i]/w[i])

# print(v)

for i in range(n):
    if W == 0:
        break
    ind = v.index(max(v))
    # print(ind)
    a = min(w[ind], W)
    amount += a*v[ind]
    W = W - a
    w[ind] = w[ind] - a

    if w[ind] == 0:
        c.pop(ind)
        v.pop(ind)
        w.pop(ind)


print(round(amount, 4))
