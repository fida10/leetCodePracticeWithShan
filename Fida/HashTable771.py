class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stonesCount = {};

        for indivStone in stones:
            if (indivStone in stonesCount):
                stonesCount[indivStone] = stonesCount[indivStone] + 1;
            else:
                stonesCount[indivStone] = 1;

        totalJewels = 0;
        for indivJewel in jewels:
            if (indivJewel in stonesCount):
                totalJewels += stonesCount[indivJewel];

        return totalJewels;