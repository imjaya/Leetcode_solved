class Solution {
public:
    struct transaction
    {
        string name, city, s_time, s_money;
        int id;
        int time, money;
        bool invalid;
        
        bool operator < (const transaction& r) const{
            
            if(this->time < r.time)
                return true;
            if(this->time > r.time)
                return false;
            return this->name.compare(r.name) <= 0;
        }
    };
    
    vector<string> invalidTransactions(vector<string>& transactions) {
     
        vector<transaction> listofTrans;
        vector<string> ans;
        
        for(int i=0; i < transactions.size(); i++)
        {
            stringstream ss(transactions[i]);
            
            transaction trans;
            
            trans.id = i;
            trans.invalid = false;
            
            getline(ss, trans.name, ',');
            getline(ss, trans.s_time, ',');
            getline(ss, trans.s_money, ',');
            getline(ss, trans.city);
            
            trans.time = stoi(trans.s_time);
            trans.money = stoi(trans.s_money);
            
            listofTrans.push_back(trans);
        }
        
        sort(listofTrans.begin(), listofTrans.end());
        
        for(int i = 0; i < listofTrans.size(); i++)
        {
            int j = i + 1;
            bool foundAny = false;
            
            while(j < listofTrans.size() &&
                  listofTrans[j].time - listofTrans[i].time <=60)
            {
                if(listofTrans[j].name == listofTrans[i].name && 
                  listofTrans[j].city != listofTrans[i].city)
                {
                    listofTrans[j].invalid = true;
                    foundAny = true;
                }
                j++;
            }
            
            if(foundAny || listofTrans[i].money > 1000)
                listofTrans[i].invalid = true;
        }
        
        for(int i = 0; i < listofTrans.size(); i++)
        {
            if(listofTrans[i].invalid)
                ans.push_back(transactions[listofTrans[i].id]);
        }
        
        return ans;
        
    }
};