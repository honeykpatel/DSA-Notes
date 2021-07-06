# DSA-Notes

## Problems
1. [Sort an array of 0’s 1’s 2’s without using extra space or sorting algo](https://github.com/honeykpatel/DSA-Notes/blob/main/Problem1.py "Problem-1")
2. [Repeated and Missing number](https://github.com/honeykpatel/DSA-Notes/blob/main/Problem2.py "Problem-2")
3. [Merge two sorted array](https://github.com/honeykpatel/DSA-Notes/blob/main/Problem3.py "Problem-3")

```python
a1 = [1,4,7,8,10]
a2 = [2,3,9]

a3 = a1+a2
a3.sort()
print(a3)

for i in range(len(a3)):
    if i<len(a1):
        a1[i] = a3[i]
    else:
        a2[i-len(a1)] = a3[i]
print(a1)
print(a2)
```

