class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        int n = s1.length();
        int m = s2.length();
        
        // If lengths don't match, it's impossible
        if (n + m != s3.length()) return false;
        
        vector<vector<bool>> dp(n + 1, vector<bool>(m + 1, false));
        
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= m; j++) {
                if (i == 0 && j == 0) {
                    dp[i][j] = true;
                } else if (i == 0) {
                    // Only s2 is available
                    dp[i][j] = dp[i][j-1] && s2[j-1] == s3[i+j-1];
                } else if (j == 0) {
                    // Only s1 is available
                    dp[i][j] = dp[i-1][j] && s1[i-1] == s3[i+j-1];
                } else {
                    // Check if s3's current char matches s1's OR s2's current char
                    dp[i][j] = (dp[i-1][j] && s1[i-1] == s3[i+j-1]) || 
                               (dp[i][j-1] && s2[j-1] == s3[i+j-1]);
                }
            }
        }
        
        return dp[n][m];
    }
};