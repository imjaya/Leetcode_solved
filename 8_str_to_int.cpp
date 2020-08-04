int myAtoi(string str) {
        long ans=0;
        int sign=1,i=0;
        while(str[i]==' ') { 
            ++i; 
        }
        if(str[i]=='-' || str[i]=='+') {
            if(str[i]=='-') sign=-1;
            else sign=1;
            ++i;
        }
        while(str[i]>='0' && str[i]<='9') {
            ans=ans*10+(str[i]-'0');
            if(ans*sign>=INT_MAX) return INT_MAX;
            if(ans*sign<=INT_MIN) return INT_MIN;   
            ++i;
        } 
        return ans*sign; 
    }