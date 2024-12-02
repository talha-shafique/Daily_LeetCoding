class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        # if len(words)==1 and s==words[0]:
        #     return True
        temp=''
        for i in range(len(words)):
            temp=temp+words[i]
            print(temp)
            if s==temp:
                return True
        return False

        