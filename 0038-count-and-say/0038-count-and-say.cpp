class Solution {
public:
    string countAndSay(int n) {
        if (n == 1) return "1";
        
        string prev = countAndSay(n - 1);  // Recursive call for previous sequence
        string result = "";
        int count = 1;

        for (int i = 1; i < prev.length(); i++) {
            if (prev[i] == prev[i - 1]) {
                count++;  // Count similar digits
            } else {
                result += to_string(count) + prev[i - 1];  // Append count and digit
                count = 1;  // Reset count
            }
        }

        result += to_string(count) + prev.back();  // Append the last group
        return result;
    }
};