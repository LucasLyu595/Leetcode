#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adj[pre].append(cur)
            indegree[cur] += 1
        leaves = [i for i in range(numCourses) if 0 == indegree[i]]
        ans = []
        coursesRemain = numCourses
        while leaves:
            cur = leaves.pop()
            coursesRemain -= 1
            ans.append(cur)
            for child in adj[cur]:
                indegree[child] -= 1
                if not indegree[child]:
                    leaves.append(child)
        if coursesRemain:
            return []
        return ans
        
        
# @lc code=end

