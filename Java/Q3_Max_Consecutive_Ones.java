class MaxConsecutiveOnes {
    public int findMaxConsecutiveOnes_myWay(int[] nums) {
        // Initialise the maxCounter and current Counter to 0.
        int maxCount = 0;
        int count = 0;

        // For Loop for each item in the Array.
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                // If `1`, update the current Counter first
                count++;
                // Then check if the current Counter is > than maxCounter.
                if (count > maxCount) {
                    // If so, replace maxCount with current Counter.
                    maxCount = count;
                }
                // Else reset the current Counter to 0.
            } else {
                count = 0;
            }
        }
        return maxCount;
    }

    public int findMaxConsecutiveOnes_btrWay(int[] nums) {
        // Step 1. Initialize maxCount and currCount.
        int maxCount = 0;
        int currCount = 0;

        // Step 2. Create For Loop.
        for (int n : nums) { // This means for each item in the array, aka n = nums[i]

            // This is a ternary operator.
            // It is a short form of an if-else statement.
            // Format:
            // condition ? valueIfTrue : valueIfFalse
            currCount = (n == 1) ? currCount + 1 : 0;
            
            // Math.max(a, b) returns the larger of the two values.
            maxCount = Math.max(maxCount, currCount);
        }

        return maxCount;
    }

    public static void main(String[] args) {
        
        MaxConsecutiveOnes maxConsecutiveOnes = new MaxConsecutiveOnes();

        int[] nums = {1, 1, 0, 1, 0, 1, 1, 1};

        int result = maxConsecutiveOnes.findMaxConsecutiveOnes_myWay(nums);
        int btr_result = maxConsecutiveOnes.findMaxConsecutiveOnes_btrWay(nums);
        System.out.println("Anwer of Max Consecutive Ones My Way: " + result);
        System.out.println("Anwer of Max Consecutive Ones Better Way: " + btr_result);
    }
}