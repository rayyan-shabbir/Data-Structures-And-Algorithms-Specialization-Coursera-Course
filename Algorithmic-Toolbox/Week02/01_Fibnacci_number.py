def fib(n):
    prv1 = 0
    prv2 = 1

    if n <= 1:
        return n

    for i in range(2, n+1):
        cur = prv1 + prv2
        prv1 = prv2
        prv2 = cur
    

    return prv2


n = int(input())

print(fib(n))
