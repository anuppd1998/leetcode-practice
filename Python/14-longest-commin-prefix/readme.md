# Longest Common Prefix
## Problem Statement
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

**Example 1:**
```
Input: strs = ["flower","flow","flight"]
Output: "fl"
```
**Example 2:**
```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 ```

**Constraints:**
- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists of only lowercase English letters if it is non-empty.

## Algorithm
*Input:*
A list of strings strs

*Output:*
The longest common prefix among all strings

---
1. If the list `strs` is empty, return empty string `""`.
2. Set `prefix` to the first string in the list.
3. For each string `st` in the list starting from the second string:
    1. While `st` does not start with `prefix`:
        - Remove the last character from `prefix`.
        - (`prefix = prefix[:-1]`)
    2. If `prefix` becomes empty, return `""`.
4. After all strings are processed, return `prefix`.

## Pseudocode: Longest Common Prefix
```python
Algorithm LongestCommonPrefix(strs)

    if strs is empty then
        return ""

    prefix ← strs[0]

    for each string st in strs starting from index 1 do

        while prefix is not empty AND st does not start with prefix do
            remove last character from prefix

        if prefix is empty then
            return ""

    return prefix

```