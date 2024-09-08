n=int(input())
for i in range(1,n+1):
    space = " " * (n-i)
    star ="* " * i
    print(space + star)

for i in range(1,n):
    space = " " * i
    star ="* " * (n-i)
    print(space + star)