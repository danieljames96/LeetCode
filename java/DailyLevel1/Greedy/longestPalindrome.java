package DailyLevel1.Greedy;

public class longestPalindrome {
    public static int longestPalindrome(String s) {
        int[] count = new int[256];
        int odds = 0;
        for (int v = 0; v < s.length(); v++) {
            char currChar = s.charAt(v);
            count[currChar] += 1;
            odds += (count[currChar] & 1) == 1 ? 1 : -1;
        }
        return s.length() - odds + (odds > 0 ? 1 : 0);

        }

    public static void main(String[] args) {
        String s = "abccccdd";
        System.out.println(longestPalindrome(s));
    }
}
