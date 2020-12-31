class Solution {
public:
    int maxNumberOfBalloons(string text) {
        vector<int>k(26,0);
        int i;
        for(i=0; text[i]!='\0'; i++)
            k[text[i]-'a']+=1;
        string s="ballon";
        vector<int>p;
        for(i=0; s[i]!='\0'; i++){
            if(s[i]=='l'||s[i]=='o')
                p.push_back(k[s[i]-'a']/2);
            else
                p.push_back(k[s[i]-'a']);
        }
        int min=p[0];
        for(i=1; i<p.size(); i++)
            if(p[i]<min)
                min=p[i];
        return min;
    }
};