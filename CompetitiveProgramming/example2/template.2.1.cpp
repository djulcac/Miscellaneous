#include<bits/stdc++.h>
using namespace std;

bool f(){cout<<"x";return true;}
bool g(){cout<<"y";return true;}
bool g2(int i,int b){cout<<i<<"-"<<b;return true;}
bool g3(int i,int a,int b){cout<<i<<"-"<<a<<'-'<<b;return true;}
typedef long long ll;
#define _int int
#define _f4(i,a,b,step) for(_int i=a;i<b;i+=step)
// #define _f3(i,a,b) for(_int i=a;i<b;i++)
// #define _f3(i,a,b) for(bool _=a<b,_int i,_?i=a:i=b;(_&&i<b)||(!_&&i>a);_?i++:i--)
// #define _f3(i,a,b) for(_int i,bool _,a<b?(_=1,i=a):(_=0,i=b);(_&&i<b)||(!_&&i>a);_?i++:i--)
// #define _f3(i,a,b) for(_int i=a<b?a:b,_=a<b;(_&&i<b&&f())||(g()&&!_&&g2(i,b)&&i>b&&g());_?i++:i--)
#define _f3(i,a,b) for(_int i=a,_=a<b;(g3(i,a,b)&&_&&i<b)||(!_&&i>b);_?i++:i--)
#define _f(i,n) for(_int i=0;i<n;i++)

ll solve(){
	_f3(i,15,12)cout<<i<<",";
	cout<<endl;
	_f(i,3)cout<<i<<" ";
	cout<<endl;
	// _f4(i,3,9,-2)cout<<i<<" ";
	// cout<<endl;
	return 0;
}

int main(){
	ll T = 1;
	// T = nxt();
	while(T--) solve();
	return 0;
}
//2