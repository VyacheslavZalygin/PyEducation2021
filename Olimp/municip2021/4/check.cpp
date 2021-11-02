#include <vector>
#include "testlib.h"

using namespace std;

int n, m;
vector<int> a, b;

long long calc_sum(long long t)
{
    long long s = 0;
    for (int i = 0; i < n; ++i)
        s += abs(a[i] + t);
    for (int i = 0; i < m; ++i)
        s += abs(b[i] - t);
    return s;
}


int main(int argc, char* argv[]) {
    registerTestlibCmd(argc, argv);

    n = inf.readInt();
    m = inf.readInt();
    a.resize(n);
    for(int i = 0; i < n; i++)
        a[i] = inf.readInt();
    b.resize(m);
    for(int i = 0; i < m; i++)
        b[i] = inf.readInt();

    long long user = ouf.readLong();
    long long corr = ans.readLong();
    if (user < 0)
        quitf(_wa, "Answer is less than 0");
    if (user > 1e10)
        quitf(_wa, "Answer is too large");

    long long user_sum = calc_sum(user);
    long long corr_sum = calc_sum(corr);

    if (user_sum == corr_sum)
        quitf(_ok, "Correct answer");
    else if (user_sum > corr_sum)
        quitf(_wa, "It is not the best answer");
    else
        quitf(_fail, "User answer is bettet, than jury answer");
}
