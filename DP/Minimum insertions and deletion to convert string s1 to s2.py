Minimum insertions and deletion to convert string s1 to s2

This is a classic DP problem and is directly related to Longest Common Subsequence (LCS).

Intuition

Suppose we want to convert

s1 = "heap"
s2 = "pea"

The common part is:

ea

(LCS = "ea")

Instead of deleting everything and rebuilding the string, we keep the LCS.

Everything not in the LCS:

must be deleted from s1
must be inserted to obtain s2
Example
heap
pea

LCS

ea

Delete from s1

heap
^^

Delete h
Delete p

Deletions = 2

Now we have

ea

Need to become

pea

Insert

p

Insertions = 1

Total operations

2 deletions
1 insertion
Observation

If

L = length of LCS

Then

Characters to delete from s1

len(s1) - L

Characters to insert into s1

len(s2) - L
Formula
Deletions = len(s1) - LCS

Insertions = len(s2) - LCS
Algorithm
Find LCS of s1 and s2.
Compute
deletions = len(s1) - lcs
insertions = len(s2) - lcs
Code
class Solution:
    def minOperations(self, s1, s2):
        m, n = len(s1), len(s2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        lcs = dp[0][0]

        deletions = m - lcs
        insertions = n - lcs

        return insertions, deletions
Example
s1 = "heap"
s2 = "pea"

ins, dels = Solution().minOperations(s1, s2)

print("Insertions:", ins)
print("Deletions:", dels)

Output:

Insertions: 1
Deletions: 2
Complexity
Time: O(m × n)
Space: O(m × n)

Key insight: The LCS is the part you can keep unchanged. Everything else in s1 must be deleted, and everything missing from s2 must be inserted. That's why the formulas are:

Deletions = len(s1) - LCS
Insertions = len(s2) - LCS
