class Solution {
public:
    int findCircleNum(vector<vector<int>>& M) {
        set<int> friends;
        for (int i = 0; i < M.size(); i++) {
            friends.emplace(i);
        }
        
        int result = 0;
        while (not friends.empty()) {
            remove_friend_circle(M, friends, *friends.begin());
            result++;
        }
        
        return result;
    }
    
    void remove_friend_circle(vector<vector<int>>& M, set<int> &friends, int removed_friend) {
        friends.erase(friends.find(removed_friend));
        for (int i = 0; i < M.size(); i++) {
            if (i == removed_friend)
                continue;
            if (friends.count(i) == 0)
                continue;
            
            if (M.at(removed_friend).at(i) == 1)
                remove_friend_circle(M, friends, i);
        }
    }
};