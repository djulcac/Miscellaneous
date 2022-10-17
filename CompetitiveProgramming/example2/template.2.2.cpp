#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define _int int
#define _f4(i,a,b,step) for(_int i=a,_=a<b,_2=abs(step);(_&&i<b)||(!_&&i>b);_?i+=_2:i-=_2)
#define _f3(i,a,b) for(_int i=a,_=a<b;(_&&i<b)||(!_&&i>b);_?i++:i--)
#define _f(i,n) for(_int i=0;i<n;i++)

ll solve(){
	_f3(i,15,12)cout<<i<<",";
	cout<<endl;
	_f(i,3)cout<<i<<" ";
	cout<<endl;
	_f4(i,3,12,2)cout<<i<<" ";
	cout<<endl;
	return 0;
}

int main(){
	ll T = 1;
	// T = nxt();
	while(T--) solve();
	return 0;
}
//2