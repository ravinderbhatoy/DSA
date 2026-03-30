#include <iostream>
#include <map>
#include <unordered_map>
using namespace std;

int main() {

  // map<string, int> mp;
  //
  // mp["apple"] = 50;
  // mp["banana"] = 150;
  // mp.emplace("kiwi", 20);
  //
  // cout << mp["apple"] << endl;
  // mp.erase("kiwi");

  // ** Multimap can store multiple same keys
  // multimap<string, int> mmp;
  //
  // mmp.emplace("apple", 50);
  // mmp.emplace("apple", 150);
  // mmp.emplace("apple", 250);
  // mmp.emplace("apple", 350);

  // mmp.erase("apple");           // this will erase all data with same key
  // mmp.erase(mmp.find("apple")); // this will only remove one occurence

  // ** unordered map (data in random order, unique values only)

  unordered_map<string, int> ump;
  ump.emplace("apple", 100);
  ump.emplace("banana", 50);
  ump.emplace("orange", 250);

  for (auto p : ump) {
    cout << p.first << ": " << p.second << endl;
  }

  return 0;
}
