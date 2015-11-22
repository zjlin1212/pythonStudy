class KMP{
public:
    vector<int> initNext(string s){
        vector<int> next(s.size(),0);
        for(int i=1,k=0;i<s.size();i++){
            while(k>0&&s[k]!=s[i])
                k=next[k-1];
            if(s[i]==s[k])
                k++;
            next[i]=k;
        }
        return next;
        
    }
    void kmp(string T,string P,vector<int> next){
        int t=0;
        for(int i=0,q=0;i<T.size();i++){
            while(q>0&&P[q]!=T[i])
                q=next[q-1];
            if(T[i]==P[q])
                q++;
            if(q==P.size())
                cout<<i-q+1<<endl;
        }

    }
};
