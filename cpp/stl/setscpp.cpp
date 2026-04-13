#include <iostream>
// #include <set>
#include <unordered_set>
using namespace std;

int main() {

  // unique values only
  // set<int> s;
  //
  // s.insert(1);
  // s.insert(1);
  // s.insert(2);
  // s.insert(3);
  // s.insert(4);
  //
  // cout << "Lower bound: " << *(s.lower_bound(2)) << endl;
  //

  unordered_set<int> us;
  us.insert(1);
  us.insert(2);
  us.insert(3);
  us.insert(4);
  us.insert(5);

  for (auto val : us) {
    cout << val << " ";
  }

  return 0;
}
