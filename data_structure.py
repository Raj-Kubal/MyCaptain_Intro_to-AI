"""Assigning elements to different lists"""

#suppose a list x
x = [0,1,2,3,4,5,6,7,8,9,10]
print(" LIST",x)

#assigning in sequence or reversing
y = x[::-1]
print(y)

#assigning using indentation
z= x[5] #instead of 5 any no. can be put but with the range and keeping in mind that it starts from 0
print(z)

#assigning or printing using for loop
z=0
for i in x:
    z=z+i
print(z)





"""Accessing elements from a tuple"""

#suppose a tuple x
x = (0,1,2,3,4,5,6,7,8,9,10)
print("\nTUPLE",x)

#assigning using indentation
print("x[0]", x[0])
print("x[1:6]",x[1:6])





"""Deleting different dictionary elements"""

#suppose a dictionary xprint(x)
x={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6}
print("\nDICTIONARY",x)

#Deleting elements
del x["f"]     #deleting the element with key "f"
print(x)

y=x.pop("a")
print(x,"\n",y)
