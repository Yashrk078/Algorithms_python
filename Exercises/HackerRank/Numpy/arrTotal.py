a =[1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
total=0
#Method 1
print(sum(a))

#Method 2 
for _ in range(len(a)):
 #    print(a[_])
    total+=a[_]

print(total)
