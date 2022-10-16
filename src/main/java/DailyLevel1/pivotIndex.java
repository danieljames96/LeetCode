package DailyLevel1;

public class pivotIndex {

    public static int rightSum(int[] nums, int indx){
        int sum=0;
        for(int i=indx+1;i<nums.length;i++){
            sum+=nums[i];
        }
//        System.out.println("RightSum:"+sum);
        return sum;
    }

    public static int leftSum(int[] nums, int indx){
        int sum=0;
        for (int i = indx - 1; i >= 0; i--) {
            sum += nums[i];
        }
//        System.out.println("LeftSum:"+sum);
        return sum;
    }

    public static int pivotIndex(int[] nums) {
        int numlength = nums.length;
        for(int i=0;i<numlength;i++){
//            System.out.println("Index:"+i);
            if (leftSum(nums,i) == rightSum(nums,i)) return i;
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] nums = {1,7,3,6,5,6};
        System.out.println(pivotIndex(nums));
    }

}
