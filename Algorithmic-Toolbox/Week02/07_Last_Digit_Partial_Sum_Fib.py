# sum of m to n => F(n+2) - F(m+1)
def fib(n):
    if n <= 1:
        return n
    
    n = n % 60

    prv1 = 0
    prv2 = 1

    for i in range(2, n+1):
        cur = (prv1 + prv2)
        prv1 = prv2
        prv2 = cur

    return prv2

            


m, n = map(int, input().split(" "))

if n <= 1:
    print(n)
else:
    fib_1 = fib(m+1)
    fib_2 = fib(n+2)
    lst = (fib_2 - fib_1) % 10
    print(lst)





