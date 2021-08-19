sum = 0
while True:
    x = int(input())
    if x%3== 0 & x%5==0:
        sum += x
        if x == 0:
            break
print (sum)