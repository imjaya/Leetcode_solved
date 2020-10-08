// TIME O(N^2) SPACE O(1)

class Solution {
public:
    int trap(vector<int>& height) {
        
        int trapped_water=0;
        
        for(int i=1;i<height.size();i++)
        {
            int left=0,right=0;
            for(int j=0;j<=i;j++)
            {
                left=max(left,height[j]);
                
            }
            for (int k=i;k<height.size();k++)
            {
                right=max(right,height[k]);
            }
            
            trapped_water+=min(left,right)-height[i];
            cout<<"left "<<left<<endl;
            cout<<"right "<<right<<endl;
            cout<<trapped_water<<endl;
            
        }
        
        
        
        return(trapped_water);
        
    }
};