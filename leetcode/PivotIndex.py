class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum1 = 0 
        lsum = [0]*len(nums)
        for i in range(0,len(nums)):
            lsum[i]=sum1
            sum1+=nums[i]
            
        for i in range (0,len(nums)):
            l_sum = 0
            r_sum = 0
            if(i==0):
                l_sum=0
            else:
                l_sum = lsum[i]
            if(i==len(nums)-1):
                r_sum = 0 
            else:
                r_sum = sum1- nums[i]-l_sum
            if(l_sum == r_sum):
                return i
        return -1
      //https://leetcode.com/problems/find-pivot-index/description/
