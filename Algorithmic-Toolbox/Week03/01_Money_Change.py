def check_rem(rem, n):
    count = 0

    if rem // n != 0:
        count += (rem//n)
        rem = rem - (rem//n)*n

    return (rem, count)


rem = int(input())
count = 0

rem, cnt = check_rem(rem, 10)
count += cnt
rem, cnt = check_rem(rem, 5)
count += cnt
rem, cnt = check_rem(rem ,1)
count += cnt



print(int(count))