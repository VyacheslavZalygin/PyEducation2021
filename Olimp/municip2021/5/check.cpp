#include <vector>
#include "testlib.h"

using namespace std;

int n;
vector<int> a;

int count(int group, int start, int finish)
{
    cout << "Group # " << group << endl;
    long long sum = 0;
    for (int i = start; i < finish; ++i)
        sum += a[i];
    cout << "Sum of all numbers in the group is " << sum << endl;
    if (sum > 0)
    {
        cout << "Group is OK" << endl << endl;
        return 1;
    }
    else
    {
        cout << "Group is BAD" << endl << endl;
        return 0;
    }
}

int main(int argc, char* argv[]) {
    registerTestlibCmd(argc, argv);

    n = inf.readInt();
    a.resize(n);
    for(int i = 0; i < n; i++)
        a[i] = inf.readInt();

    int n1, n2, n3, corr;

    n1 = ouf.readInt(0, n);
    corr = ans.readInt(0, n);

    if (n1)
    {
        n2 = ouf.readInt(1, n);
        n3 = ouf.readInt(1, n);
        if (n1 + n2 + n3 != n)
            quitf(_wa, "Sum of three numbers must be equal to N");
        int c = 0;
        c += count(1, 0, n1);
        c += count(2, n1, n1 + n2);
        c += count(3, n1 + n2, n);
        if (c < 2)
        {
            quitf(_wa, "There is only %d groups, where party X wins ", c);
        }
        else
        {
            if (corr == 0)
                quitf(_fail, "Jury answer is impossible, but solution exists");
            else
                quitf(_ok, "OK - solution exists");
        }
    }
    else
    {
        if (corr == 0)
        {
            quitf(_ok, "OK - no solution");
        }
        else
        {
            quitf(_wa, "User answer is 0, but solution exists");
        }
    }
}
