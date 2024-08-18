# Sum of F(n) = F(n+2) - 1

def sumlastdig(n):
    prv1 = 0
    prv2 = 1

    if n <= 1:
        return n
    else:
        n = (n+2) % 60

    for i in range(2, n+1):
        cur = prv1 + prv2
        prv1 = prv2
        prv2 = cur

    lst = (prv2-1) % 10
    return lst


n = int(input())
lst = sumlastdig(n)
print(lst)