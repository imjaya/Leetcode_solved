class Solution {
public:
    
    void dfs(vector<string> &res, string str,string digits,int l,unordered_map<char,vector<char>>m){
        if(str.length()==digits.length()){
            res.push_back(str);
            return;
        }
        char c = digits[l];
        for(auto j=m[c].begin();j!=m[c].end();j++){
            dfs(res,str+(*j),digits,l+1,m);
        }
    }
    
    vector<string> letterCombinations(string digits) {
        unordered_map<char,vector<char>>m;
        m['2'].insert(m['2'].begin(),{'a','b','c'});
        m['3'].insert(m['3'].begin(),{'d','e','f'});
        m['4'].insert(m['4'].begin(),{'g','h','i'});
        m['5'].insert(m['5'].begin(),{'j','k','l'});
        m['6'].insert(m['6'].begin(),{'m','n','o'});
        m['7'].insert(m['7'].begin(),{'p','q','r','s'});
        m['8'].insert(m['8'].begin(),{'t','u','v'});
        m['9'].insert(m['9'].begin(),{'w','x','y','z'});
        
        // for(auto i=m.begin();i!=m.end();i++){
        //     for(int j=0;j<i->second.size();j++){
        //         cout<<i->second[j]<<" ";
        //     }
        //     cout<<endl;
        // }
        vector<string> res;
        if(!digits.size())
            return res;
        dfs(res,"",digits,0,m);
        return res;
    }
};