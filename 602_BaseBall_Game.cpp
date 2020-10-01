class Solution {
public:
    int calPoints(vector<string>& ops) {
        vector<int> q;
        for(string s : ops){
            switch(s[0]){
                case 'C':
					if(q.empty()) break;
                    q.pop_back(); break;
                case '+':
                    switch(q.size()){
                        case 0: break;
                        case 1: q.emplace_back(q.back()); break;
                        default:
                            auto itend = q.end() - 1;
                            q.emplace_back(*itend + *(itend - 1));
                            break;
                    } break;
                case 'D':
                    if(q.empty()) break;
                    q.emplace_back(q.back() * 2); break;
                default :
                    q.emplace_back(std::stoi(s)); break;
            }
        }        
        int sum = 0;
        for(int x : q){
            sum += x;
        }
        return sum;
    }
};