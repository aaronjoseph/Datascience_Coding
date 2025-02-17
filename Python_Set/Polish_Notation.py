from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in "+-*/":
                # Push numbers onto the stack
                stack.append(int(token))
            else:
                # Pop the two topmost elements as operands
                right = stack.pop()
                left = stack.pop()
                # Perform the corresponding operation
                if token == "+":
                    stack.append(left + right)
                elif token == "-":
                    stack.append(left - right)
                elif token == "*":
                    stack.append(left * right)
                elif token == "/":
                    # Use int() for truncation towards zero
                    stack.append(int(left / right))
        # The final result is the only element left in the stack
        return stack[0]

# Example usage:
solution = Solution()
tokens = ["2", "1", "+", "3", "*"]
print(solution.evalRPN(tokens))  # Expected output: 9