// #include <deque>
#include <iostream>
#include <vector>
using namespace std;
// #include <list>

int main() {

  // ** list **

  // list<int> l;
  // l.push_back(1);
  // l.push_back(2);
  // l.push_front(3);
  // l.push_front(5);
  // l.pop_back();
  // l.pop_front();
  // for (int ele : l) {
  //   cout << ele << " ";
  // }
  //
  // cout << l[2] << endl; **not possible

  // ** Deque **
  // deque<int> q = {1, 2, 3, 4};
  // cout << q[2] << endl;

  // ** Pair **

  pair<int, int> p = {2, 4};
  pair<char, pair<int, int>> p1 = {'a', {2, 3}};
  vector<pair<int, int>> vp = {{1, 2}, {3, 4}, {5, 6}};

  cout << p.first << endl;
  cout << p.second << endl;

  cout << p1.first << endl;
  cout << p1.second.first << endl;

  vp.push_back({7, 8});  // insert
  vp.emplace_back(9, 0); // inplace  object create (will determine datatype)

  return 0;
}
