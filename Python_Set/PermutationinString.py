from typing import List


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = [0] * 26
        s2Count = [0] * 26

        # Build the frequency counts for s1 and the first window of s2.
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # Slide the window over s2.
        for i in range(len(s2) - len(s1)):
            # Check if the current window's frequency matches s1's frequency.
            if s1Count == s2Count:
                return True
            # Slide the window: remove the character going out and add the new character.
            s2Count[ord(s2[i]) - ord('a')] -= 1
            s2Count[ord(s2[i + len(s1)]) - ord('a')] += 1

        # Check the last window after the loop.
        return s1Count == s2Count


# Example Usage:
solution = Solution()

# Example 1:
s1 = "ab"
s2 = "eidbaooo"
print(f"checkInclusion({s1}, {s2}) -> {solution.checkInclusion(s1, s2)}")
# Expected output: True, because "ba" (a permutation of "ab") is present in s2.

# Example 2:
s1 = "ab"
s2 = "eidboaoo"
print(f"checkInclusion({s1}, {s2}) -> {solution.checkInclusion(s1, s2)}")
# Expected output: False, because no permutation of "ab" exists in s2.

# Additional Example:
s1 = "adc"
s2 = "dcda"
print(f"checkInclusion({s1}, {s2}) -> {solution.checkInclusion(s1, s2)}")
# Expected output: True, because "cda" (a permutation of "adc") is present in s2.