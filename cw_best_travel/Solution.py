from itertools import combinations


def choose_best_sum(t: int(), k: int(), ls: list()) -> int():
    all_combos = {sum(i) if sum(i) <= t else 0 for i in combinations(ls, k)}
    return max(all_combos) if sum(all_combos) != 0 else None


print(
    choose_best_sum(
        430,
        8,
        [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89],
    )
)
