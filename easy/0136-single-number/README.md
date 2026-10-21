# Single Number

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a **non-empty** array of integers `nums`, every element appears *twice* except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

**Example 1:**

**Input:** nums = [2,2,1]

**Output:** 1

**Example 2:**

**Input:** nums = [4,1,2,1,2]

**Output:** 4

**Example 3:**

**Input:** nums = [1]

**Output:** 1

 

**Constraints:**

- 1 <= nums.length <= 3 * 104
- -3 * 104 <= nums[i] <= 3 * 104
- Each element in the array appears twice except for one element which appears only once.

## Solution

**Language:** Python  
**Runtime:** 9 ms (beats 18.63%)  
**Memory:** 21.4 MB (beats 25.48%)  
**Submitted:** 2026-10-21T10:37:45.161Z  

```py
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        counts = {} 
        for num in nums: 
            counts[num] = counts.get(num, 0) + 1 
        
        for num, count in counts.items(): 
            if count == 1: 
                return num



        
```

---

[View on LeetCode](https://leetcode.com/problems/single-number/)