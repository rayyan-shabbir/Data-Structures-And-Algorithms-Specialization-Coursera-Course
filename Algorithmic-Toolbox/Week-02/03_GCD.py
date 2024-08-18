a, b = map(int, input().split(" "))

mx = max(a, b)
mn = min(a, b)

rem = -1

while rem != 0:
    rem = mx % mn
     
    if rem == 0:
        break

    mx = mn
    mn = rem

print(mn)