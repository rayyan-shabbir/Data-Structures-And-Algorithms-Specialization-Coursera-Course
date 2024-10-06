def fib_mod_10(n):
    # Pisano period for modulo 10 is 60
    pisano_period = 60
    n = n % pisano_period

    prv1, prv2 = 0, 1

    if n <= 1:
        return n

    for i in range(2, n+1):
        cur = (prv1 + prv2)
        prv1, prv2 = prv2, cur

    return prv2 % 10

n = int(input())

print(fib_mod_10(n))
