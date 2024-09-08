n=int(input())

for i in range(n):
    space=" " * i
    if i == 0:
        print("+ " * n)
    else:
        star="* " * (n-i)
        print(space+ star)
        