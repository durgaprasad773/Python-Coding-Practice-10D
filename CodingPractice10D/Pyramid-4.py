n=int(input())
for i in range(1,n+1):
    row = (str(i) + " ") * i
    print(row)
for i in range(1,n):
    row = (str(n-i) + " ") * (n-i)
    print(row)