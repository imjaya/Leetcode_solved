class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aliceSizes.sort()
        bobSizes.sort()
        alice_sum = sum(aliceSizes)
        bob_sum = sum(bobSizes)
        #Binary search approach
        for alice in aliceSizes:
            b_l = 0
            b_r = len(bobSizes) - 1
            while(b_l <= b_r):
                b_m = (b_l + b_r) // 2
                bob = bobSizes[b_m]
                if alice_sum - alice + bob == bob_sum - bob + alice:
                    return [alice, bob]
                elif alice_sum - alice + bob < bob_sum - bob + alice:
                    b_l = b_m + 1
                else:
                    b_r = b_m - 1