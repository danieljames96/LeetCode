package DailyLevel1;

import java.util.Arrays;

public class runningSum {

    public static int sum(int[] nums, int i){

        int sum;

        if(i >= 0){
            sum=nums[i];
            return sum+=sum(nums,i-1);
        }
        else{
            return 0;
        }
    }

    public static int[] runningSum(int[] nums) {
        int numsize = nums.length;
        int[] runningsum = new int[numsize];
        for (int i = 0; i < numsize; i++) {
            runningsum[i] = sum(nums,i);
        }
        return runningsum;
    }

    public static void main(String[] args) {
        int[] nums = {1,2,3,4,5};
        System.out.println(Arrays.toString(runningSum(nums)));
    }
}
