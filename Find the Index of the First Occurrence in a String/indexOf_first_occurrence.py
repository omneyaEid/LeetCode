class Solution(object):
    def strStr(self, haystack, needle):

        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1


calling_class = Solution()

result = calling_class.strStr("sadbutsad", "sad")
print("index of the first occurrence is  ", result)
