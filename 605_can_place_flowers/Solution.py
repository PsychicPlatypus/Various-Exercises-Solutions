class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        for _ in range(n):
            if len(flowerbed) == 0:
                return False
            for j in range(len(flowerbed)):
                if flowerbed == [0]:
                    flowerbed.pop()
                    break
                if len(flowerbed) <= 1:
                    return False
                if j == 0 and [flowerbed[j], flowerbed[j + 1]] == [0, 0]:
                    flowerbed.pop(0)
                    flowerbed.pop(0)
                    break
                if [flowerbed[len(flowerbed) - 1], flowerbed[len(flowerbed) - 2],] == [
                    0,
                    0,
                ]:
                    print("here")
                    flowerbed.pop(-1)
                    flowerbed.pop(-1)
                    break
                if j == len(flowerbed) - 2:
                    return False
                if len(flowerbed) <= 2:
                    return False
                if [flowerbed[j], flowerbed[j + 1], flowerbed[j + 2]] == [0, 0, 0]:
                    flowerbed = flowerbed[j + 3 : len(flowerbed)]
                    break

        return True
