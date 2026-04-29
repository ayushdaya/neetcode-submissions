from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]


        def isAnagram(a, b) -> bool:
            return Counter(a) == Counter(b)
        
        counter = [0]*len(strs)
        counter[0] = 1
        anagram_dict = {}
        anagram_dict[strs[0]] = [strs[0]]

        for i in range(1,len(strs)):
            for word in anagram_dict.keys():
                if isAnagram(strs[i], word):
                    anagram_dict[word].append(strs[i])
                    counter[i] = 1
            if counter[i] == 0:
                anagram_dict[strs[i]] = [strs[i]]
        final_list = []

        for i in anagram_dict.keys():
            final_list.append(anagram_dict[i])

        return final_list
            