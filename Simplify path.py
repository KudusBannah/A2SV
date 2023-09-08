class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = ["/"]
        path = path.split("/")
        for dirs in path:
            if dirs == "..":
                if len(stack) > 1: stack.pop()
            elif dirs != "." and dirs != "":
                stack.append(dirs+"/")

        output = "".join(stack)
        if len(output) > 1:
            return output[:-1]
        return output