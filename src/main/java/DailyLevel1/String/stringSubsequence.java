package DailyLevel1.String;

public class stringSubsequence {
    public static boolean isSubsequence(String s, String t) {
        int startIndx=0, indx = 0;
        for (int i = 0; i < s.length(); i++) {
            indx = t.indexOf(s.charAt(i),startIndx);
            if (indx == -1) return false;
            else startIndx = indx+1;

            if (startIndx == t.length() && i < s.length()-1) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        String s = "axc", t = "ahbgdc";
        System.out.println(isSubsequence(s,t));
    }
}
