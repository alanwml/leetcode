import java.util.Arrays;

class ShuffleTheArray {
    public int[] shuffle_MyWay(int[] nums, int n) {
        if (nums.length == 2 * n){

            int x[] = new int[n];
            int y[] = new int[n];
            int ans[] = new int[2*n];

            // Step 1. Create the 'x' and 'y' arrays.
            for (int i = 0; i < n; i++) {
                x[i] = nums[i];
                y[i] = nums[n+i];
            }
            
            // Step 1.5. Create a x & y count for the for loop.
            int x_count = 0;
            int y_count = 0;

            // Step 2. Create the ans array by Modulo-ing 2.
            // If Even, use X Array.
            // If Odd, use Y Array.
            for (int j = 0; j < nums.length; j++){
                if (j % 2 == 0) {
                    ans[j] = x[x_count];
                    x_count++;
                } else {
                    ans[j] = y[y_count];
                    y_count++;
                }
            }

            // System.out.println("Array X: " + Arrays.toString(x));
            // System.out.println("Array Y: " + Arrays.toString(y));
            // System.out.println("Answer: " + Arrays.toString(ans));
            return ans;
        }
        else{
            System.out.println("Nums Length does not equals to 2 * n.");
            return new int[] {1, 2};
        }
    }

    public int[] shuffle_BetterWay(int[] nums, int n) {
        int len = nums.length;
        int[] ans = new int[len];

        for (int i = 0; i < len; i++) {
            if (i % 2 == 0) {
                ans[i] = nums[i / 2];
            } else {
                ans[i] = nums[n + (i / 2)];
            }
        }
        
        return ans;
    }

    public static void main(String[] args) {
        
        int[] nums = {1, 2, 1, 2};
        // int[] nums = {1, 2, 3, 4, 4, 3, 2, 1};
        int n = 2;
        ShuffleTheArray shuffleTheArray = new ShuffleTheArray();
        int[] result = shuffleTheArray.shuffle_MyWay(nums, n); 
        int[] btr_result = shuffleTheArray.shuffle_BetterWay(nums, n);
        System.out.println("Anwer of Shuffle The Array My Way: " + Arrays.toString(result));
        System.out.println("Anwer of Shuffle The Array Better Way: " + Arrays.toString(btr_result));
    }
}