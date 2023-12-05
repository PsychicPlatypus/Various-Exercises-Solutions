class Solution:
    def numberOfMatches(self, n: int) -> int:
        total = self.get_matches(n, 0)
        return int(total)

    def get_matches(self, teams: int, matches: int) -> int:
        if teams == 1:
            return matches

        if teams % 2 == 0:
            matches += teams / 2
            return self.get_matches(teams / 2, matches)
        else:
            matches += (teams - 1) / 2
            return self.get_matches((((teams - 1) / 2) + 1), matches)


"""
n
if even
    total += n/2
    advance = n/2
if uneven
    total += n-1 /2
    advance = ((n-1) / 2) + 1

total
"""
