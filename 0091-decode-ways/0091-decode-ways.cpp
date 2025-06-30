class Solution {
public:
    int decode(int i,string& s,vector<int>& dp){
        if(i==s.size()){
            return 1;
        }
        if(s[i]=='0'){
            return 0;
        }
        if(dp[i]!=-1) {
            return dp[i];
        }
        int res=decode(i+1,s,dp);
        if(i+1<s.size()){
            int twodigit=stoi(s.substr(i,2));
            if(9<twodigit && twodigit<27){
                res+=decode(i+2,s,dp);
            }
        }
        dp[i]=res;
        return dp[i];
    }
    int numDecodings(string s) {
        vector<int>dp(s.size()+1,-1);
        return decode(0,s,dp);
    }
};