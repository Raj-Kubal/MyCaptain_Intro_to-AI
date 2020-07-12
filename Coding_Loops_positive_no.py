list1 = list()
list1 = [int(x) for x in input("Please Enter the number").split()]
for num in list1:
    if num<0:
        list1.remove(num)
print(list1)
