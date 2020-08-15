class Solution {
public:
    bool isValid(string s) {
        
        if(!s.size()) return true;
        stack<int> brackets;
        
        for(int i=0; i<s.size(); i++){
            
            char c = s[i];
            if(c=='(' or c=='{' or c=='[') brackets.push(c);
            else if(brackets.empty() and (c==')' or c=='}' or c==']')) brackets.push(c);
            else {
                if(c==')' and brackets.top()=='(') brackets.pop();
                else if(c=='}' and brackets.top()=='{') brackets.pop();
                else if(c==']' and brackets.top()=='[') brackets.pop();
                else brackets.push(c);
            }
        }
        return brackets.empty()? true: false;
    }
};