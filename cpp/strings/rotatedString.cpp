#include <bits/stdc++.h>
using namespace std;

bool rotatedString(string s, string goal)
{
    if (s.size() != goal.size())
    {
        return false;
    }
    int i = 0, j = 0;
    int n = s.size();

    while (i < n && s[i] != goal[j])
        i++;

    return true;
}

int main()
{

    string s = "abcde";
    string goal = "cdeab";

    return 0;
}