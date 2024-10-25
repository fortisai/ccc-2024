#include<iostream>
#include<map>
 
using namespace std;
 
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    map<string, int> m;
    int n; cin >> n;
    string s;
    while(n--) {
        cin >> s;
        if(m.find(s) == m.end()) m[s] = 0;
        else m[s]++;
        if(m[s] == 0) cout << "OK" << endl;
        else cout << s << m[s] << endl;
    }
    return 0;
}