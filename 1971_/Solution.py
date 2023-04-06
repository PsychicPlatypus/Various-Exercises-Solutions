from typing import List


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        if edges == [] or n == 1:
            return True
        if source >= n or destination >= n:
            return False

        connected_nodes = set()

        while True:
            if len(edges) == 0:
                return False
            if len(connected_nodes) == 0:
                for i in edges:
                    if source in i:
                        connected_nodes.add(i[0])
                        connected_nodes.add(i[1])
                        edges.remove(i)
                        break
                else:
                    return False
            else:
                for i in edges:
                    if i[0] in connected_nodes or i[1] in connected_nodes:
                        connected_nodes.add(i[0])
                        connected_nodes.add(i[1])
                        edges.remove(i)
                        break
                else:
                    return False

            if destination in connected_nodes:
                return True


print(
    Solution().validPath(
        10,
        [
            [0, 7],
            [0, 8],
            [6, 1],
            [2, 0],
            [0, 4],
            [5, 8],
            [4, 7],
            [1, 3],
            [3, 5],
            [6, 5],
        ],
        7,
        5,
    )
)
