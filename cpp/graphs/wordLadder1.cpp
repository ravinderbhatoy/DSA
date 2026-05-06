#include <iostream>
#include <queue>
#include <string>
#include <unordered_set>
using namespace std;

int ladderLength(string beginWord, string endWord, vector<string> wordList) {
  queue<pair<string, int>> q;
  unordered_set<string> st(wordList.begin(), wordList.end());
  q.push({beginWord, 1});

  while (!q.empty()) {
    string word = q.front().first;
    int steps = q.front().second;
    q.pop();

    if (word == endWord)
      return steps;

    for (int i = 0; i < word.size(); i++) {
      char original = word[i];
      for (char ch = 'a'; ch <= 'z'; ch++) {
        word[i] = ch;
        if (st.find(word) != st.end()) {
          st.erase(word);
          q.push({word, steps + 1});
        }
      }
      word[i] = original;
    }
  }
  return 0;
}

int main() {

  string beginWord = "hit";
  string endWord = "cog";

  vector<string> wordList = {"hot", "dot", "dog", "log", "lot", "cog"};

  cout << ladderLength(beginWord, endWord, wordList) << endl;

  return 0;
}
