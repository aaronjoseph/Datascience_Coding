class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}  # Closing to Opening mapping

        for char in s:
            if char in bracket_map:  # If it's a closing bracket
                top_element = stack.pop() if stack else '#'  # Pop or use a dummy character
                if top_element != bracket_map[char]:  # Check for valid match
                    return False
            else:
                stack.append(char)  # Push open brackets onto stack

        return not stack  # Return True if stack is empty (all brackets matched)

solution = Solution()
# print(solution.isValid("()"))
print(solution.isValid("()[]{}"))
# print(solution.isValid("(]"))
# print(solution.isValid("([])"))