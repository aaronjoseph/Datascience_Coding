class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Dictionary to count frequency of characters in the current window.
        count = {}
        max_count = 0  # Maximum frequency of any character in the current window.
        left = 0  # Left pointer for the sliding window.
        result = 0  # Maximum length of a valid window.

        # Expand the window with the right pointer.
        for right, char in enumerate(s):
            # Update the count for the current character.
            count[char] = count.get(char, 0) + 1

            # Update max_count to the highest frequency in the window.
            max_count = max(max_count, count[char])

            # Check if the number of characters that need to be replaced
            # exceeds k. That is: (window size) - (count of the most frequent char) > k.
            if (right - left + 1) - max_count > k:
                # If so, shrink the window from the left.
                count[s[left]] -= 1
                left += 1

            # Update the result with the current window size.
            result = max(result, right - left + 1)

        return result


# Example usage:
solution = Solution()

# Example 1:
s = "ABAB"
k = 2
# Explanation: Replace the two 'A's with 'B's or vice versa to get "BBBB" or "AAAA".
print(f"characterReplacement({s}, {k}) -> {solution.characterReplacement(s, k)}")
# Expected output: 4

# Example 2:
s = "AABABBA"
k = 1
# Explanation: Replace the one 'A' in the middle to form "AABBBBA". The longest substring is "BBBB", of length 4.
print(f"characterReplacement({s}, {k}) -> {solution.characterReplacement(s, k)}")
# Expected output: 4


def characterReplacement(self, s: str, k: int) -> int:
    l = 0
    c_frequency = {}
    longest_str_len = 0
    for r in range(len(s)):
        if not s[r] in c_frequency:
            c_frequency[s[r]] = 0
        c_frequency[s[r]] += 1
        cells_count = r - l + 1
        if cells_count - max(c_frequency.values()) <= k:
            longest_str_len = max(longest_str_len, cells_count)
        else:
            c_frequency[s[l]] -= 1
            if not c_frequency[s[l]]:
                c_frequency.pop(s[l])
            l += 1

    return longest_str_len
