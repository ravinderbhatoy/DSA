#include "iostream"
#include <queue>
// #include <stack>
using namespace std;

int main() {

  // stack<int> st;
  //
  // st.push(1);
  // st.push(2);
  // st.push(3);
  //
  // stack<int> st2;

  // swap values of one stack to other
  // st.swap(st2);
  //
  // while (!st.empty()) {
  //   cout << st.top() << " ";
  //   st.pop();
  // }

  // cout << "Size of st: " << st.size() << endl;
  // cout << "Size of st2: " << st2.size() << endl;

  // queue<int> q;
  // q.push(1);
  // q.push(2);
  // q.push(3);
  //
  // while (!q.empty()) {
  //   cout << q.front() << " ";
  //   q.pop();
  // }
  //
  //
  // q.swap()

  priority_queue<int> pq;

  pq.push(5);
  pq.push(3);
  pq.push(10);
  // descending order (maxHeap)
  while (!pq.empty()) {
    cout << pq.top() << " ";
    pq.pop();
  }
  cout << endl;

  priority_queue<int, vector<int>, greater<int>> pqa;
  pqa.push(5);
  pqa.push(3);
  pqa.push(10);

  // ascending order (minHeap)
  while (!pqa.empty()) {
    cout << pqa.top() << " ";
    pqa.pop();
  }

  return 0;
}
