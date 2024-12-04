/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    void reorderList(ListNode* head) {
        if(!head || !head->next){
            return;
        }
        ListNode* slow = head;
        ListNode* fast = head->next;
        while(fast && fast->next){
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* cur = slow->next;
        slow->next = nullptr;

        ListNode* pre = nullptr;
        ListNode* t = nullptr;
        while(cur){
            t = cur->next;
            cur->next = pre;
            pre = cur;
            cur = t;
        }
        cur = head;

        while(pre){
            t = pre->next;
            pre->next = cur->next;
            cur->next = pre;
            cur = pre->next;
            pre = t;
        }
    }
};