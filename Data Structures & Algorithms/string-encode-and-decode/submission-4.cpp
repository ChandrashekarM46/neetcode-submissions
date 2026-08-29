class Solution {
public:

    string encode(vector<string>& strs) {
    string res="";

    for(auto c : strs)
    {
        res+=to_string(c.length()) + '#' + c;
    }
    return res;
    }

    vector<string> decode(string s) {
    int i=0;
    vector<string> res;

    while(i<s.length())
    {
        int j=i;

        while(s[j]!='#')
         j++;
        
        int len = stoi(s.substr(i,j-i));
        
        string word = s.substr(j+1,len);
        res.push_back(word);

        i=j+1+len;
    }
    return res;
    }
};
