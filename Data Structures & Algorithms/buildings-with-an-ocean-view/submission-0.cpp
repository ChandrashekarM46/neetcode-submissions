class Solution {
public:
    vector<int> findBuildings(vector<int>& heights) {
    int maxl=0;
    vector<int> ans;
    for (int i=heights.size()-1;i>=0;i--)
    {
        if (heights[i]>maxl)
         ans.push_back(i);
        maxl=max(maxl,heights[i]);
    }
    reverse(ans.begin(),ans.end());
    return ans;
    }
};