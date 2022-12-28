class Solution(object):
    @staticmethod
    def romanToInt(s):
        char_list = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        operate = []
        for i in range(len(s) - 1):
            if s[i] == "I" or s[i] == "X" or s[i] == "C":
                position = True
                for j in range(i + 1, len(s)):
                    if char_list[s[j]] > char_list[s[i]]:
                        operate.append(-1 * char_list[s[i]])
                        position = False
                        break
                if position:
                    operate.append(char_list[s[i]])
            else:
                operate.append(char_list[s[i]])
        operate.append(char_list[s[-1]])
        return sum(operate)