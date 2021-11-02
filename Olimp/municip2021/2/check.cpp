#include <bits/stdc++.h>
#include "testlib.h"

using namespace std;

struct mirror{
   int x, y;
   string d;
   mirror(int x, int y, string d)
   {
       this->x = x;
       this->y = y;
       this->d = d;
   }
};

vector <mirror> mirrors;
int N, NA, X, Y;

bool found = false;
void findWay(int a, int b, int dx, int dy, int len = 0)
{
    if (len > N || found) return;

    for (mirror m : mirrors)
    {
        if ((m.x != a || m.y != b) && ((m.x - a) * dx == (m.y - b) * dy) && (m.x - a) * dx > 0)
        {
            if (m.d == "H") findWay(m.x, m.y,  dx, -dy, len+1);
            else if (m.d == "V") findWay(m.x, m.y, -dx,  dy, len+1);
            else if (m.d == "E") found = true;
        }
    }
}

const int MAX = 100000;
int main(int argc, char* argv[])
{
   registerTestlibCmd(argc, argv);

    X = inf.readInt(-MAX, MAX, "X");
    Y = inf.readInt(-MAX, MAX, "Y");
    N = ouf.readInt(-1, MAX, "N");
    NA = ans.readInt(-1, MAX, "NA");
    
    if (N != NA)
        quitf(_wa, "Wrong number of mirrors");
    if (N < 1 && NA < 1 && N == NA)
        quitf(_ok, "OK. No mirrors or no solution");
    
    for(int i = 0; i < N; i++)
    {
        int x, y;
        string d;
        x = ouf.readInt(-MAX, MAX);
        y = ouf.readInt(-MAX, MAX);
        d = ouf.readWord("[VH]");
        
        if (x == 0 && y == 0)
            quitf(_wa, "Mirror at the point (0, 0)");

        for(mirror m: mirrors){
            if (x == m.x && y == m.y){
                quitf(_wa, "Mirrors are at the same position:(%d, %d)", x, y);
            }
        }
        mirrors.push_back(mirror(x, y, d));
    }
    mirrors.push_back(mirror(X, Y, "E"));
    findWay(0, 0, 1, 1, 0);
    if (found)
    {
        quitf(_ok, "OK");
    }
    else
    {
        quitf(_wa, "Wrong mirrors");
    }
}
