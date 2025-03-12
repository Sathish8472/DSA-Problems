public class NumArray {

    int _left;
    int _right;
    private int[] _nums;
    int _length;
    public NumArray(int[] nums) {
        _nums= nums;
    }
    
    public int SumRange(int left, int right) {
        int sum = 0;
        for(int i = left; i <= right; i++){
            sum = sum + _nums[i];
        }

        return sum;
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.SumRange(left,right);
 */