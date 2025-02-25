def lengthOfLongestSubstring(s: str) -> int:
    char_map = {}
    left = 0
    max_len = 0
    for right, value in enumerate(s):
        if value in char_map and char_map[value] >= left:
            left = char_map[value] + 1
        char_map[value] = right
        max_len = max(max_len, right - left + 1)
    return max_len


lengthOfLongestSubstring("abcabcbb")
