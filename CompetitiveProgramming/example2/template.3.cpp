#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define _int int
#define _f4(i,a,b,step) for(_int i=a,_=a<b,_2=abs(step);(_&&i<b)||(!_&&i>b);_?i+=_2:i-=_2)
#define _f3(i,a,b) for(_int i=a,_=a<b;(_&&i<b)||(!_&&i>b);_?i++:i--)
#define _f(i,n) for(_int i=0;i<n;i++)

// #define f,a,b _f(a,b)
// #define $a cout<<a;
// #define $$ cout<<endl;
#define _p(a,b) cout<<a<<" "<<b;
#define P(t) cout<<t;
#define p(a) cout<<a<<endl;
// #define $ cout<<endl;
// #define v(...) cout<<

// print
#define p(a) cout<<t;
#define P(a) cout<<t<<endl;
#define p1(a) cout<<t;
#define P1(a) cout<<t<<endl;
#define p2(a,b) cout<<t;
#define P2(a,b) cout<<t<<endl;

ll solve(){
	_f3(i,3,6)cout<<i<<" ";cout<<endl;
	ll a=3;
	_p(3,4);
	cout<<"bien"<<endl;
	// $a;
	cout<<endl;
	// for(int a=0;a<3;a++)$a
	// P((1,3,4))
	// p(45)
	cout<<"gg"<<endl;
	// cout<<__VA_ARGS__<<endl;
	return 0;
}

int main(){
	ll T = 1;
	// cin>>T;
	while(T--) solve();
	// while(T--) cout<<solve()<<endl;
	return 0;
}
//3
/*
https://stackoverflow.com/questions/679979/how-to-make-a-variadic-macro-variable-number-of-arguments
http://gcc.gnu.org/onlinedocs/cpp/Variadic-Macros.html
https://stackoverflow.com/questions/2124339/c-preprocessor-va-args-number-of-arguments
https://stackoverflow.com/questions/63559297/unable-to-run-c17-program-in-vscode
*/