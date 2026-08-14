class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        words.reverse()
        return " ".join(words)


obj = Solution()

s = "the sky is blue"

answer = obj.reverseWords(s)

print(answer)


#without using builtin functions except reverse
class Solution(object):
    def reverseWords(self, s):
        word=""
        words=[]
        for ch in s:
            if ch !=" ":
                word+=ch
            else:
                if word!="":
                    words.append(word)
                    word=""
        if word!="":
            words.append(word)
        words.reverse()          
        result=""
        for i in range(len(words)):
            result+=words[i]
            if i!=len(words)-1:
                result += " "
        return result
                    
                
obj = Solution()

s = "the sky is blue"

answer = obj.reverseWords(s)

print(answer)


#without using any built in functions
class Solution(object):
    def reverseWords(self, s):
        word = ""
        words = []

        for ch in s:
            if ch != " ":
                word += ch
            else:
                if word != "":
                    words.append(word)
                    word = ""

        if word != "":
            words.append(word)

        rev = ""

        for i in range(len(words) - 1, -1, -1):
            rev += words[i]

            if i != 0:
                rev += " "

        return rev
obj = Solution()

s = "the sky is blue"

answer = obj.reverseWords(s)

print(answer)