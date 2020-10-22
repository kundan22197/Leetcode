class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        st = ''
        l = path.split('/')
        l = ' '.join(l).split()
        i = 0
        while i < len(l):
            if stack and l[i] == '..':
                stack.pop()
            elif l[i] not in ['.', '..']:
                stack.append(l[i])
            i += 1
        st = '/' + '/'.join(stack)
        return st