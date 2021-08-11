#this functions calculates nCr
def c(n,r):
    if n==r or r==0:
        return 1
    elif r==1 or r==n-1:
        return n
    else:
        res = 1
        for i in range(r):
            res*= n-i
            res/=i+1
        return int(res)
   
n = 5     
for i in range(n+1):
    for j in range(i+1):
        print('{} '.format(c(i,j)), end='')
        
    print('\n')
