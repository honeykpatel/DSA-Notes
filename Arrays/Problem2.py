#Repeated and Missing number

#Method 1 : Hashing

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


#Method 2 : Sum and Sum of squares

l1 = [3,2,1,1,5] 

n = len(l1)

#S1 is sum of n numbers
S1 = int((n*(n+1))/2)
#S2 is sum of squares of n numbers
S2 = int((n*(n+1)*(2*n + 1)/6))

#s1 is sum of numbers in given list
s1 = sum(l1)
#s2 is sum of squares of numbers in given list
s2 = sum([x**2 for x in l1])

#taking difference of both the sums 
diff1 = S1-s1
diff2 = S2-s2

#x-y will be diff1 and x^2 - y^2 will be diff2, where x is repeated and y is missing
x = (((diff2)/(diff1)) + (diff1))/2
y = x-diff1

print(f'{int(x)} is repeating and {int(y)} is missing')
