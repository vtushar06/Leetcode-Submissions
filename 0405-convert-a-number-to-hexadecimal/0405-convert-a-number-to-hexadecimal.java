public class Solution {
    public String toHex(int num) {
        if (num == 0) return "0";

        char[] hexChars = {'0','1','2','3','4','5','6','7','8','9',
                           'a','b','c','d','e','f'};
        StringBuilder hex = new StringBuilder();

        // Treat as unsigned using 32 bits
        while (num != 0 && hex.length() < 8) {
            int digit = num & 0xf; // Get last 4 bits
            hex.insert(0, hexChars[digit]); // Append corresponding hex digit
            num >>>= 4; // Unsigned right shift (fills with 0)
        }

        return hex.toString();
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.toHex(26));  // Output: "1a"
        System.out.println(s.toHex(-1));  // Output: "ffffffff"
    }
}