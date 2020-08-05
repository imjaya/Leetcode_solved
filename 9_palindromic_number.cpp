//static auto x = []() {ios_base::sync_with_stdio(false); cin.tie(NULL); return NULL;}();
#include <cmath>
class Solution {
public:
    bool isPalindrome(int x) {
        if (x<0) return false;
        int y=0,z=x;
        short int n;
        while( z!=0 ){
            n = z%10;
            if ( y > (INT_MAX/10 - n) ) return false;
            y = y*10 + n;
            z /= 10;
        }
        return (x==y);
    }
};