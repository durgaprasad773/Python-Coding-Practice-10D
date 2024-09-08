n=int(input())
for i in range(1,n+1):
    space = "  " * (n-i)
    row = ("+ " * (i-1)) + "#"
    print(space + row)

for i in range(1,n):
    space = "  " * i
    row = ("+ " * (n-i-1)) + "#"
    print(space + row)