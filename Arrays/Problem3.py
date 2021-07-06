#Method 1 : Using extra array

a1 = [1,4,7,8,10]
a2 = [2,3,9]

a3 = a1+a2
#sorting the 3rd array
a3.sort()
print(a3)

#putting sorted values back in both arrays
for i in range(len(a3)):
    if i<len(a1):
        a1[i] = a3[i] #first values will go in a1
    else:
        a2[i-len(a1)] = a3[i] #rest in a2
print(a1)
print(a2)

#Method 2 : Using Insertion based sortng

a1 = [1,4,7,8,10]
a2 = [2,3,9]

for i in range(len(a1)):
    if a2[0]<a1[i]:
        a2[0],a1[i]=a1[i],a2[0]
        a2.sort()
    else:
        continue

print(a1)
print(a2)
