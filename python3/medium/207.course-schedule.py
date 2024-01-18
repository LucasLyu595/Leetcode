#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        tree, indegree = dict(), [0] * numCourses
        for (cur, pre) in prerequisites:
            if pre in tree:
                tree[pre].append(cur)
            else:
                tree[pre] = [cur]
            indegree[cur] += 1
        roots = []
        for i in range(len(indegree)):
            if indegree[i]: continue
            roots.append(i)
        while roots:
            root = roots.pop(0)
            if root not in tree:
                continue
            children = tree.pop(root)
            for child in children:
                indegree[child] -= 1
                if indegree[child] == 0:
                    roots.append(child)
        return len(tree) == 0

# @lc code=end

