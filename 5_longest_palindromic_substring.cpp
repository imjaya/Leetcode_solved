class Solution {
    
public:
    string expand(string str, int low, int high)
    {
        int length = str.length();
               
       
        while((low >= 0) && (high < length) && (str[low] == str[high]))
        {
            low = low - 1;
            high = high + 1;
         }      
        return(str.substr(low + 1,high-low-1)); //(high-low-1) is the length of substring
     }
    
    string longestPalindrome(string s) {
        string max_str = "";
        int max_length = 0;
        for(int i=0;i<s.length();i++)
        {
            //find a longest odd length palindrome with str[i] as mid point
            string curr_str = expand(s, i, i);
            int curr_length = curr_str.length();
            //update maximum length palindromic substring if odd length
            //palindrome has greater length
            if(curr_length > max_length)
            {
                max_length = curr_length;
                max_str = curr_str;
            }
            //find a longest even length palindrome with str[i] and str[i+1] as mid points
            //Note that a even length palindrome has two mid points
            curr_str = expand(s, i, i + 1);
            curr_length = curr_str.length();
            //update maximum length palindromic substring if even length
            //palindrome has greater length
            if(curr_length > max_length)
            {
                max_length = curr_length;
                max_str = curr_str;
                }
        

            } 
    return(max_str);
    }
};