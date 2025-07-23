class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size();
        int start = 0, maxLen = 1;

        // Helper lambda function to expand around center
        auto expand = [&](int left, int right) {
            while (left >= 0 && right < n && s[left] == s[right]) {
                if (right - left + 1 > maxLen) {
                    maxLen = right - left + 1;
                    start = left;
                }
                left--;
                right++;
            }
        };

        for (int i = 0; i < n; ++i) {
            expand(i, i);     // Odd length palindrome
            expand(i, i + 1); // Even length palindrome
        }

        return s.substr(start, maxLen);
    }
};