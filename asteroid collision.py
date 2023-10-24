class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            stack.append(asteroid)
            while len(stack) > 1 and stack[-2] > 0 and stack[-1] < 0:
                survived = None
                if abs(stack[-1]) > abs(stack[-2]):
                    survived = stack[-1]
                elif abs(stack[-2]) > abs(stack[-1]):
                    survived = stack[-2]
                stack.pop()
                stack.pop()
                if survived: stack.append(survived)
        return stack