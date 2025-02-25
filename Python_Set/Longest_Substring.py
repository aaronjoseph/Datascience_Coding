def lengthOfLongestSubstring(s: str) -> int:
    # Dictionary to keep track of the last index of each character
    char_index = {}
    max_length = 0
    left = 0  # Left pointer of the sliding window

    # Iterate over the string with the right pointer
    for right, char in enumerate(s):
        # If the character is in the dictionary and is within the current window,
        # move the left pointer to one position right of the last occurrence.
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1

        # Update the character's latest index
        char_index[char] = right

        # Update the maximum length found so far
        max_length = max(max_length, right - left + 1)

    return max_length


# Example usage:
print(lengthOfLongestSubstring("abcabcbb"))  # Output: 3 (Longest substring "abc")
print(lengthOfLongestSubstring("bbbbb"))  # Output: 1 (Longest substring "b")
print(lengthOfLongestSubstring("pwwkew"))  # Output: 3 (Longest substring "wke")