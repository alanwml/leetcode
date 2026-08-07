class ConcatenationOfArray {

    public int[] getConcatenation_MyWay(int[] nums) {
        var result = new int[2 * nums.length];
        for (int i = 0; i < result.length; i++) {
            // System.out.println(i);
            if (i > nums.length - 1) {
               result[i] = nums[i - nums.length];
            }
            else {
                result[i] = nums[i];
            }
        }
        // System.out.println(java.util.Arrays.toString(result));
        return result;
    }

    public int[] getConcatenation_BetterWay(int[] nums){
        int ans[] = new int[2 * nums.length];
        for (int i = 0; i < ans.length; i++) {
            ans[i] = nums[i % nums.length];
            // Better way uses Modulo (Which means Remainder after Dividing)
        }
        return ans;
    }

    public static void main(String[] args) {
        ConcatenationOfArray concatenationOfArray = new ConcatenationOfArray();
        // int[] nums = {1, 2, 1};
        int[] nums = {1, 3, 2, 1};
        int[] MyWay = concatenationOfArray.getConcatenation_MyWay(nums);
        int[] BetterWay = concatenationOfArray.getConcatenation_BetterWay(nums);
        System.out.println("Concatenated array My Way: " + java.util.Arrays.toString(MyWay));
        System.out.println("Concatenated array Better Way: " + java.util.Arrays.toString(BetterWay));
    }
}