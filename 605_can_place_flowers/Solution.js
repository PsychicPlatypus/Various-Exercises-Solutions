/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function (flowerbed, n) {
    for (let _ = 0; _ < n; _++) {
        if (flowerbed.length == 0) return false;
        for (let i = 0; i < flowerbed.length; i++) {
            if (JSON.stringify(flowerbed) == JSON.stringify([0])) {
                flowerbed.pop();
                break;
            }
            if (flowerbed.length <= 1) return false;
            if (i == 0 && (JSON.stringify))
        }
    }
};
