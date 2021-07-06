a = [2,5,9,6,9,3,8,9,7,1]

#initialize fast and slow pointer
fast = a[0]
slow = a[0]

while True:
    slow = a[slow] #slow will take one step
    fast = a[a[fast]] #fast will take two steps
    if slow==fast: #collision
        break

fast = a[0] #move fast to initial

while True:
    slow=a[slow] #take one step
    fast=a[fast] #take one step
    if slow==fast: #number found
        break
print(slow)
