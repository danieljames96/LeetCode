class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to prereq list
        premap = { i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            premap[crs].append(pre)
        
        # Visit all courses along the curr DFS path
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if premap[crs] == []:
                return True

            visitSet.add(crs)
            for pre in premap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            premap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True