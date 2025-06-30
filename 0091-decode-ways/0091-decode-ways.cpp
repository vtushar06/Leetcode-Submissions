class Solution {
public:
    int numDecodings(string s) {
        int n=s.size();
        vector<int>dp(n+1);
        if(n==0 || s[0]=='0'){
            return 0;
        }
        dp[0]=1;
        dp[1]=1;
        // i am running accroding to dp 
        for(int i=2;i<=n;i++){
            if(s[i-1]!='0'){
                dp[i]+=dp[i-1];
            }
            int twodigit=stoi(s.substr(i-2,2));
            if(9<twodigit && twodigit<27){
                dp[i]+=dp[i-2];
            }
        }
        return dp[n];
       
    }
};