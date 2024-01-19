class Solution {
    public int removeElement(int[] nums, int val) {
        if(nums.length == 1 && nums[0] == val)
        return 0;
    int i=0,count=0;
    while(i<=nums.length-1){
        if(nums[i] == val){
            count++;
            for(int j=i; j<nums.length-1; j++)
                nums[j] = nums[j+1];
            nums[nums.length-1] = -1;
            continue;
        }
        i++;
    }
    return nums.length-count;
}
}
            