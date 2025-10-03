class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        int n=points.size();
        sort(begin(points),end(points));
        int prevend=points[0][1];
        int count=1;
        for(int i=1;i<n;i++){
            if(prevend<points[i][0]){
                count+=1;
                prevend=points[i][1];
            }
            else{
                prevend=min(prevend,points[i][1]);
            }
        }
        return count;
    }
};