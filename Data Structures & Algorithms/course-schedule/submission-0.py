class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap={i:[] for i in range(numCourses)}
        for a,b in prerequisites:
            premap[a].append(b)
        vset=set()
        def dfs(a):
            if a in vset:
                return False
            if premap[a]==[]:
                return True
            vset.add(a)
            for b in premap[a]:
                if not dfs(b):return False
            vset.remove(a)
            premap[a] == []
            return True
        for a in range(numCourses):
            if not dfs(a):return False
        return True

            


        