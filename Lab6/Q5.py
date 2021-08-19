x = int(input("enter number ="))
count = 1
sum = 0
y = 0
while count<=x:
    if count%2!= 0:
        sum += count
        y=y+1
    count +=1
mean = sum/y
print("sum of odd is =",sum)
print("mean values of sum odd = %2.f"%mean)