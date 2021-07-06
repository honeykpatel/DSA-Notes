#Sort an array of 0s, 1s and 2s

class Solution:
    def problem1(self, nums):
        #initializing values of low,mid,high
        low = 0
        mid = 0
        high = len(nums)-1
        
        while mid<=high:
          #when mid is 0 we swap mid and low, and increase mid and low
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1
          #when mid is 1 we increase mid
            elif nums[mid]==1:
                mid+=1
          #when mid is 2 we swap mid and high, and decrease high
            elif nums[mid]==2:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
        return nums
      
s = Solution()
print(s.problem1([0,1,1,0,1,2,1,2,0,0,0,1]))
