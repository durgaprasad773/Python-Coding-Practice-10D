n=int(input())
for i in range(1,n+1):
    space = "  " * (n-i)
    star = "* " * i
    row =  star + space + space +star
    print(row)
for i in range(1,n):
    space = "  " * i
    star = "* " * (n-i)
    row =  star + space + space +star
    print(row)