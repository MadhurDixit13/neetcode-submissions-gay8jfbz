class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[b].append(a)

        state = [0] * numCourses
        order = []

        def dfs(node):
            if state[node] == 1:
                return False
            if state[node] == 2:
                return True

            state[node] = 1

            for nei in graph[node]:
                if not dfs(nei):
                    return False

            state[node] = 2
            order.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return order[::-1]