a = int(input())
b = int(input())
k = int(input())

for i in range(a,k+1):
    if i % a == 0  and i % b == 0:
        print(i)
