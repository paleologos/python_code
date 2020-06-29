# IF nesting
x= "Cisco"
if "i" in x:
    if len(x)>3:
        print(x, len(x))
# FOR Nesting
list1=[4,5,6]
list2=[10,20,30]
for i in list1:
    for j in list2:
        print(i*j)
#WHILE Nesting
y=1
while y<= 10:
    z=5
    y+=1
    while z<=10:
        print(z)
        z+=1

# IF -- FOR
for i in range(12):
    if 8<=i<=11:
        print(i) 