vendors=["Cisco", "HP", "Nortel", "Avaya", "Juniper"]
equipment={"Vendor":"Cisco", "Model":"2960", "Ports":"48"}
# sekvenca- lista
for each_vendor in vendors:
    print(each_vendor)
    #sekvenca - string
    for char in each_vendor:
        print(char)

#ranges
r=range(10)
for i in r:
    print(i*2)

lr= range(len(vendors))
for i in lr:
    print(vendors[i])

for i, e in enumerate(vendors):
    print(i,e)

for e in vendors:
    print(e)
else:
    print("The end of the list")