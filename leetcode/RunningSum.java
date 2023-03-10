class Solution {
    public int[] runningSum(int[] nums) {
        //int s = nums.sum();
        int t=0;
        int res[]= new int[nums.length];
        // for(int)
        for (int i=0;i<nums.length;i++){
            t = t+nums[i];
            res[i] = t;


        }
        return res;
    }
}
//https://leetcode.com/problems/running-sum-of-1d-array/description/?envType=study-plan&id=level-1
