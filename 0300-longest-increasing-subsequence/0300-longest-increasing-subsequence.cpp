#include <bits/stdc++.h>
using namespace std;


#define pb push_back
#define F first
#define S second
#define all(x) x.begin(), x.end()
#define srt(x) x.begin(), x.end()
#define rsrt(x) x.rbegin(), x.rend()
typedef vector<int> vi;
typedef pair<int, int> pii;

class Solution {
public:
    vector<vector<int>> dp;

    int find(int i, int previdx, int n, vector<int>& a) {
        if (i >= n) return 0;

        if (dp[i][previdx + 1] != -1) return dp[i][previdx + 1];

        // Not take the current element
        int ans = find(i + 1, previdx, n, a);

        // Take the current element if it's increasing
        if (previdx == -1 || a[i] > a[previdx]) {
            ans = max(ans, 1 + find(i + 1, i, n, a));
        }

        return dp[i][previdx + 1] = ans;
    }

    int lengthOfLIS(vector<int>& a) {
        int n = a.size();
        dp.assign(n, vector<int>(n + 1, -1));
        return find(0, -1, n, a);
    }
};


