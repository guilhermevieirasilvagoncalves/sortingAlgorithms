#include <bits/stdc++.h>

using namespace std;

void insertionsort(vector<int>& v){
    int chave, i;
    
    for (int j = 0; j < v.size(); j++)
    {
        chave = v[j];
        i = j -1;
        while (i >= 0 and v[i] > chave)
        {
            v[i+1] = v[i];
            i--;
        }
        v[i+1] = chave;
    }
    
}

int main()
{
    vector<int> v = {4,2,3,1};
    insertionsort(v);
    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i] << " ";
    }
    cout << endl;
    
}
