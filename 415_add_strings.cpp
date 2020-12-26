#include<string>
class Solution {
public:
    string addStrings(string num1, string num2) {
    int i = num1.size() - 1;
    int j = num2.size() - 1;
    int sum = 0;
    string res = "";
    while (i >= 0 || j >= 0 || sum) {
        if (i >= 0 && j >= 0) { sum += (num1[i--] - '0') + (num2[j--] - '0'); }
        else if (i >= 0) { sum += num1[i--] - '0'; }
        else if (j >= 0) { sum += num2[j--] - '0'; }
        res += sum % 10 + '0';
        sum /= 10;
    }
    reverse(begin(res), end(res));
    return res;
}
};