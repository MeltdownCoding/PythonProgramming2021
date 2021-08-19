sumodd = 0
sumeven = 0
while True:
    x = int(input())
    if x == 0:
        break
    elif x%2== 0:
        sumeven += x
    elif x%2!=0:
        sumodd += x          
print(sumeven)
print(sumodd)