class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            word_freq_s = {}
            word_freq_t = {}

            for char in s:
                if char in word_freq_s.keys():
                    word_freq_s[char] +=1
                else:
                    word_freq_s[char] = 1
            for char in t:
                if char in word_freq_t.keys():
                    word_freq_t[char] +=1
                else:
                    word_freq_t[char] = 1
            for key in word_freq_s.keys():
                if key not in word_freq_t.keys():
                    return False
                if word_freq_s[key] != word_freq_t[key]:
                    return False
            return True
        else:
            return False