n=int(input("Please Enter no. of Integer to be printed: "))
series = [0]
last_num = 0
prev_num = 1
for i in range(1,n):
    next_num = last_num
    last_num = last_num + prev_num
    series.append(last_num)
    prev_num = next_num

print(series[:n])
