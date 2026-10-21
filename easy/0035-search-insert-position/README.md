# Search Insert Position

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

 

**Example 1:**

```
Input: nums = [1,3,5,6], target = 5
Output: 2

```

**Example 2:**

```
Input: nums = [1,3,5,6], target = 2
Output: 1

```

**Example 3:**

```
Input: nums = [1,3,5,6], target = 7
Output: 4

```

 

**Constraints:**

- 1 <= nums.length <= 104
- -104 <= nums[i] <= 104
- nums contains distinct values sorted in ascending order.
- -104 <= target <= 104

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.9 MB (beats 43.42%)  
**Submitted:** 2026-10-21T08:45:56.861Z  

```py
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1 
        while left <= right: 
            midpoint = (left + right) // 2
            if nums[midpoint] == target:
                return midpoint 
            if nums[midpoint] < target: 
                left = midpoint + 1 
            else: 
                right = midpoint - 1 

        return left
        
```

---

[View on LeetCode](https://leetcode.com/problems/search-insert-position/)