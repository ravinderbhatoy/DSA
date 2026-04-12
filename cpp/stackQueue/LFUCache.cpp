#include <bits/stdc++.h>
using namespace std;

class LRUCache {
public:
  struct Node {
    int key;
    int val;

    Node *next;
    Node *prev;

    Node(int key1, int val1) {
      key = key1;
      val = val1;
    }
  };

  // dummy tail and head nodes
  Node *head = new Node(-1, -1);
  Node *tail = new Node(-1, -1);

  int cap;
  unordered_map<int, Node *> umap;

  LRUCache(int capacity) {
    cap = capacity;
    head->next = tail;
    tail->prev = head;
  }

  // insert node after the head
  void addNode(Node *newNode) {
    Node *temp = head->next;
    newNode->next = temp;
    newNode->prev = head;
    head->next = newNode;
    temp->prev = newNode;
  }

  void deleteNode(Node *delNode) {
    Node *delPrev = delNode->prev;
    Node *delNext = delNode->next;
    delPrev->next = delNext;
    delNext->prev = delPrev;
  }

  int get(int key) {
    if (umap.find(key) != umap.end()) {
      Node *resNode = umap[key];
      int res = resNode->val;

      // Just move it, don't erase/re-insert into map
      deleteNode(resNode);
      addNode(resNode);
      return res;
    }
    return -1;
  }

  void put(int key, int value) {
    if (umap.find(key) != umap.end()) {
      Node *existingNode = umap[key];
      deleteNode(existingNode); // Now safe to delete since we update map
      umap.erase(key);          // Erase old pointer
    }

    if (umap.size() == cap) {
      Node *lru = tail->prev;
      umap.erase(lru->key);
      deleteNode(lru);
      delete lru; // Free the memory
    }

    Node *newNode = new Node(key, value);
    addNode(newNode);
    umap[key] = newNode;
  }
};

// Driver code
int main() {
  // Create cache with capacity 2
  LRUCache cache(2);

  // Put values in cache
  cache.put(1, 1);
  cache.put(2, 2);

  // Get value for key 1
  cout << cache.get(1) << endl;

  // Insert another key (evicts key 2)
  cache.put(3, 3);

  // Key 2 should be evicted
  cout << cache.get(2) << endl;

  // Insert another key (evicts key 1)
  cache.put(4, 4);

  // Key 1 should be evicted
  cout << cache.get(1) << endl;

  // Key 3 should be present
  cout << cache.get(3) << endl;

  // Key 4 should be present
  cout << cache.get(4) << endl;

  return 0;
}
