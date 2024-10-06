def pisano_period(m):
    prv1 = 0
    prv2 = 1

    for i in range(m*m):
        prv1, prv2 = prv2, (prv1 + prv2) % m

        if prv1 == 0 and prv2 == 1:
            return i + 1
        

def fib(n, perd):
    n = n % perd

    if n <= 1:
        return n

    prv1 = 0
    prv2 = 1

    for i in range(2, n+1):
        cur = (prv1 + prv2)
        prv1 = prv2
        prv2 = cur

    return prv2

        

n, m = map(int, input().split(" "))
perd = pisano_period(m)
# print(perd)

n = fib(n, perd)

print(n % m)
