class Solution {
public:
    vector<string> fizzBuzz(int n) 
    {
        vector<string> fizzBuzz_;
        
        for(int i = 1; i <= n; i++) 
        {
            string str = "";
            
            if(i % 3 == 0)
                str += "Fizz";
            
            if(i % 5 == 0)
                str += "Buzz";
            
            if(str == "")
                str = to_string(i);
            
            fizzBuzz_.push_back(str);
        }
		
        return fizzBuzz_;
     }
};