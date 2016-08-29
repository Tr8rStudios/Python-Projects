distinct = int(input())

temp = list(map(int,input().split()))
temp.sort()

curMax = -100

for i in range(len(temp)-1):
    x = temp[i]
    for j in range(len(temp)-1,0,-1):
        y = temp[j]
        if i != j:
            if x + y > curMax:
                curMax = x - y

print(curMax)