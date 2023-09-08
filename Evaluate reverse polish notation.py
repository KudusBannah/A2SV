class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def operation(x, y, op):
            if op == "+":
                return x + y
            elif op == "-":
                return x - y
            elif op == "*":
                return x*y
            else:
                return int(x/y)

        operations = set(["+", "-", "*", "/"])
        stack = []
        for item in tokens:
            if item in operations:
                a = stack.pop()
                b = stack.pop()
                stack.append(operation(b, a, item))
            else:
                stack.append(int(item))
        return stack[-1]