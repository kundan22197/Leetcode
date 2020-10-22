class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        l = [0] * len(T)
        stack = []
        for i in range(len(T)-1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                l[i] = stack[-1] - i
            stack.append(i)
        return l
        