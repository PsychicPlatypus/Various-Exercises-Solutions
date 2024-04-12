from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """
        Students -> Queue
        San -> Stack

        Args:
            students (List[int]): _description_
            sandwiches (List[int]): _description_

        Returns:
            int: _description_
        """
        res = 0
        cycle = 0

        while len(students) > 0:
            if cycle == len(students):
                return len(students)

            curr = students[-1]
            if curr == sandwiches[0]:
                students.pop()
                sandwiches.pop(0)
                cycle = 0
            else:
                stu = students.pop()
                students.insert(0, stu)
                cycle += 1

        return res


print(Solution().countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]))
