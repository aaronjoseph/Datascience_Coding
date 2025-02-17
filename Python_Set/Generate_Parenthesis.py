from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current: str, open_count: int, close_count: int) -> None:
            # If the current string is complete (length == 2 * n), add to results
            if len(current) == 2 * n:
                result.append(current)
                return

            # If we can add an opening parenthesis, do so
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            # Only add a closing parenthesis if it won't break the validity
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result


# Example Usage:
sol = Solution()
print(sol.generateParenthesis(3))