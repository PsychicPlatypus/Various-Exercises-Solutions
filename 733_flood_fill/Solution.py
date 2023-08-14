from typing import List


class Solution:
    def fillStar(self, image, sr, sc, fill_color, original_color):
        for i in [-1, 1]:
            if (
                sr + i >= 0
                and sr + i < len(image)
                and image[sr + i][sc] == original_color
                or image[sr + i][sc] == fill_color
            ):
                image[sr + i][sc] = fill_color
            if (
                sc + i >= 0
                and sc + i < len(image[0])
                and image[sr][sc + i] == original_color
                or image[sr][sc + i] == fill_color
            ):
                image[sr][sc + i] = fill_color
        return image

    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        if not image[sr][sc] == color:
            original_color = image[sr][sc]
            image = self.fillStar(image, sr, sc, color, original_color)
            for i in [-1, 1]:
                if (x
                    sr + i >= 0
                    and sr + i < len(image)
                    and image[sr + i][sc] == original_color
                    or image[sr + i][sc] == color
                ):
                    image = self.fillStar(image, sr + i, sc, color, original_color)
                if (
                    sc + i >= 0
                    and sc + i < len(image[0])
                    and image[sr][sc + i] == original_color
                    or image[sr][sc + i] == color
                ):
                    image = self.fillStar(image, sr, sc + i, color, original_color)

            print(image)
        return image


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
color = 2

Solution().floodFill(image, sr, sc, color)
