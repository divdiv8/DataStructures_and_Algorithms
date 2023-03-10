class Solution {
    public int finalValueAfterOperations(String[] operations) {
        int x =0;
        for(String i : operations){
            if(i.equals("X++") || i.equals("++X"))
            x++;
            else
            x--;
        }
        return x;
    }
}

//https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/
