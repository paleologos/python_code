# for break
for i in range(10):
    if i==7:
        break
    print(i)

l1=[4,5,6]
l2=[10,20,30]
for i in l1:
    for j in l2:
        if j==20:
            break
        print(i*j)
    print("Out of loop 2")