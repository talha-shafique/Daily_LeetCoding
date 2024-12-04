class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        p=0
        s=''
        if len(str1)<len(str2):
            return False
        else:
            for i in str1:
                print('i',i)
                while p<len(str2):
                    print('p',p)
                    if i=='z' and str2[p]=='a':
                        s=s+str2[p]
                        p=p+1
                        break
                    elif i==str2[p] or ord(i)+1==ord(str2[p]):
                        print('orig i',i)
                        s=s+str2[p]
                        print('updated i',i)
                        p=p+1
                        break
                    else:
                        print('no luck!')
                        break
            
        print(s)
        print(str2)
        if s == str2:
            return True
        else:
            return False

        

        
        

        

        