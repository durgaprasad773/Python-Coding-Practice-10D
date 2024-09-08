n=int(input())
for i in range(1,n+1):
    space =" " * (n-i)
    num =(str(i)+" ") * i
    print(space + num)
