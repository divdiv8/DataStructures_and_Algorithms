class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        int[] temp = nums;
        int i=0;
        int j=0;
        int[] x=new int[2];
        for (i=0;i<nums.length;i++) {
            for(j=0;j<nums.length;j++)
            {
                if(nums[i]+nums[j]==target && i!=j)
                   { x[0]=i;
                    x[1]=j;
                    return x;
                    }


            }

            
    }
    return x;
}
}

/** https://leetcode.com/problems/two-sum/description/*/
