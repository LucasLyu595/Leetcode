#
# @lc app=leetcode id=269 lang=python3
#
# [269] Alien Dictionary
#

# @lc code=start
from collections import defaultdict, deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        prefix = {}
        prefix['*'] = []
        for word in words:
            cur = prefix
            for c in word:
                if c not in cur:
                    cur[c] = {}
                    cur[c]['*'] = []
                if c in cur['*']: 
                    if c != cur['*'][-1]:
                        return ""
                else:
                    cur['*'].append(c)
                cur = cur[c]
            if len(cur['*']) > 0:
                return ""
        
        graph = defaultdict(set)
        children = set()
        heads = set()
        queue = deque()
        queue.append(prefix)
        while queue:
            curMap = queue.popleft()
            cur = curMap['*']
            prev = ""
            for c in cur:
                if not prev:
                    heads.add(c)
                else:
                    if prev != c:
                        graph[prev].add(c)
                        children.add(c)
                prev = c
                queue.append(curMap[c])

        headsFiltered = set()
        for c in heads:
            if c not in children:
                headsFiltered.add(c)

        rankMap = defaultdict(int)
        rank = 0
        queue = deque()
        
        for head in headsFiltered:
            visited = defaultdict(int)
            def dfs(cur: str) -> bool:
                for child in graph[cur]:
                    state = visited[child]
                    if 1 == state:
                        return False
                    if 2 == state:
                        continue
                    visited[child] = 1
                    if not dfs(child):
                        return False
                    visited[child] = 2
                return True
            if not dfs(head):
                return ""

            queue.append(head)
            while queue:
                cur = queue.popleft()
                rankMap[cur] = rank
                for child in graph[cur]:
                    queue.append(child)
                rank += 1
        res = "".join(sorted(list(rankMap.keys()), key=lambda x: rankMap[x]))
        if len(res) < len(headsFiltered) + len(children):
            return ""
        return res

# @lc code=end

