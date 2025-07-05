class Solution {
public:
vector<vector<int>> dp;

vector<int>c;
int minimumcost(int i,int j){
  if(i+1==j) return 0;
  if(dp[i][j]!=-1) return dp[i][j];
  int ans=INT_MAX;
  for(int k=i+1;k<j;k++){
    int cost= minimumcost(i,k)+minimumcost(k,j)+c[j]-c[i];
    ans=min(ans,cost);
    
  }
  return dp[i][j]=ans;
}
  
    int minCost(int n, vector<int>& cuts) {
        cuts.push_back(0);
        cuts.push_back(n);
        sort(cuts.begin(),cuts.end());
        c=cuts;
        // memset(dp,-1,sizeof(dp));
        int sz = cuts.size();
        dp.assign(sz, vector<int>(sz, -1));
        return minimumcost(0,c.size()-1);
    }
};