package DailyLevel1.Greedy;

public class maxProfit {
    public static int maxProfit(int[] prices) {
        int length = prices.length;
        int lsf = Integer.MAX_VALUE;
        int op = 0, tp = 0;


        if(length == 0 || length == 1){
            return 0;
        }
        else if (length == 2){
            if(prices[0] > prices[1]){
                return 0;
            }
            else{
                return prices[1] - prices[0];
            }
        }

        for (int i = 0; i < length; i++) {
            if(prices[i] < lsf){
                lsf = prices[i];
            }
            tp = prices[i] - lsf;
            if(tp > op){
                op = tp;
            }
        }

        return op;
    }

    public static void main(String[] args) {
        int[] prices = {7,1,5,3,6,4};
        System.out.println(maxProfit(prices));
    }
}
