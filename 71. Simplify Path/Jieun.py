class Solution:
    def simplifyPath(self, path: str) -> str:
        paths=[p for p in path.split('/') if p]
        stack=[]
        ans=''
        for p in paths:
            if p=='..':
                if stack: 
                    stack.pop()
            elif p!='.':
                stack.append(p)

        if not stack:
            return "/"
        for p in stack:
            ans+='/'+p
        return ans
        # return '/'+'/'.join(stack)
        # this one looks more cool but it's more time consuming