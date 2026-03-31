x = int(input())

n = len(str(x))
start = False

for i in range(n):
    digit = x % 10
    x //= 10

    if digit != 0:
        start = True

    if start:
        print(digit, end="")