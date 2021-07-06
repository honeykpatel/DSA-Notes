#Repeated and Missing number

l1 = [3,3,1,5,2]

#creating hash table
l2 = [0 for x in range(len(l1)+1)]

#noting repeatation of numbers by its index 
for i in l1:
    l2[i] += 1

#traversing through hash values
for i in range(1,len(l2)):
    #if repeated
    if l2[i] == 2:
        x = i
    #if missing
    elif l2[i]==0:
        y = i
        
print(f'{x} is repeating and {y} is missing')
