# Remove Linked List Elements

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given the `head` of a linked list and an integer `val`, remove all the nodes of the linked list that has `Node.val == val`, and return *the new head*.

 

**Example 1:**

```
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

```

**Example 2:**

```
Input: head = [], val = 1
Output: []

```

**Example 3:**

```
Input: head = [7,7,7,7], val = 7
Output: []

```

 

**Constraints:**

- The number of nodes in the list is in the range [0, 104].
- 1 <= Node.val <= 50
- 0 <= val <= 50

## Solution

**Language:** Python  
**Runtime:** 2 ms (beats 52.87%)  
**Memory:** 22.5 MB (beats 43.17%)  
**Submitted:** 2026-10-21T11:00:34.268Z  

```py
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        # Create a dummy node pointing to the head
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        curr = head
        
        while curr is not None:
            if curr.val == val:
                # Skip the node by pointing prev to the node after curr
                prev.next = curr.next
            else:
                # Only move prev forward if we didn't delete curr
                prev = curr
            
            # Always move curr forward
            curr = curr.next
            
        # Return whatever is after our dummy node as the new head
        return dummy.next
```

---

[View on LeetCode](https://leetcode.com/problems/remove-linked-list-elements/)