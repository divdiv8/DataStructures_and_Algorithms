def count_subarrays(arr):
# Write your code here
    stack1 = deque()
    stack2= deque()
    result = [1]*len(arr)
    for i in range(0,len(arr)):
#loop i to 0
        print(i)
        stack1.clear()
        stack2.clear()
        stack1.append(arr[i])
        stack2.append(arr[i])
        for j in range(i,-1,-1):
            print(j,'j 1')
            if arr[j]>arr[i]:
                stack1.clear()
                break
            elif i!=j:
                stack1.append(arr[j])
                result[i]+=1
                #print(result,'result 1')
        #print('still in i')
        for j in range(i,len(arr)):
            print(j,'j 2')
            if arr[j]>arr[i]:
                stack2.clear()
                break
            elif i!=j:
                stack2.append(arr[j])
                result[i]+=1
                #print(result,'result 2')
        #print('still in i 2')    
    return result



###Contiguous Subarrays
# You are given an array arr of N integers. For each index i, you are required to determine the number of contiguous subarrays that fulfill the following conditions:
# The value at index i must be the maximum element in the contiguous subarrays, and
# These contiguous subarrays must either start from or end on index i.
# Signature
# int[] countSubarrays(int[] arr)
# Input
# Array arr is a non-empty list of unique integers that range between 1 to 1,000,000,000
# Size N is between 1 and 1,000,000
# Output
# An array where each index i contains an integer denoting the maximum number of contiguous subarrays of arr[i]
# Example:
# arr = [3, 4, 1, 6, 2]
# output = [1, 3, 1, 5, 1]
# Explanation:
# For index 0 - [3] is the only contiguous subarray that starts (or ends) at index 0 with the maximum value in the subarray being 3.
# For index 1 - [4], [3, 4], [4, 1]
# For index 2 - [1]
# For index 3 - [6], [6, 2], [1, 6], [4, 1, 6], [3, 4, 1, 6]
# For index 4 - [2]
# So, the answer for the above input is [1, 3, 1, 5, 1]

