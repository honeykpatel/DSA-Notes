#Kadane's Algorithm

a = [-2,-3,4,-1,-2,1,5,-3]
#initializing sum and maxi
s = 0
maxi = a[0]

for i in range(len(a)):
    #adding element to the sum
    s += a[i]
    #if s greater than maxi then change maxi
    if s > maxi:
        maxi=s
    #if s is less than maxi
    else:
        #if s less than zero then make it zero
        if s<0:
            s=0
print(maxi)
