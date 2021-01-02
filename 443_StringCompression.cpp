class Solution {
public:
    int compress(vector<char>& chars) {
        int i = 0;              // current index
        int index = 0;          // solution index 
        while(i < chars.size()){
            char current = chars[i];
            int count = 1;
            while(++i < chars.size() && chars[i] == current){
                count++;
            }
            chars[index++] = current;
            if(count > 1){
                for(char& ch : to_string(count)){
                    chars[index++] = ch;
                }
            }
        }
        return index;
    }
};