n=int(input())
for i in range(1,n+1):
    space = " " * (n-i)
    mid_space = "  " * (n-i)
    star = "* " * i
    print(space + star + mid_space + star)