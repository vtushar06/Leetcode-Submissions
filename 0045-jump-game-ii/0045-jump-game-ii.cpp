class Solution {
public:
    int jump(vector<int>& nums) {
        int n=nums.size();
        vector<int> dp(n+1,n);
        dp[0]=0;
        for(int i=1;i<n;i++){
            for(int j=0;j<i;j++){
                if(nums[j]+j>=i){
                    dp[i]=min(dp[j]+1,dp[i]);
                }
            }
        }
        return dp[n-1];
        
    }
};