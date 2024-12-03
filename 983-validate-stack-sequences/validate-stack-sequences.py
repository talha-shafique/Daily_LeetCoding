class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        i=0
        for j in pushed:
            print('j',j)
            stack.append(j)
            while stack and stack[-1]==popped[i]:
                stack.pop()
                print(stack)
                i=i+1
        if stack:
            return False
        else:
            return True