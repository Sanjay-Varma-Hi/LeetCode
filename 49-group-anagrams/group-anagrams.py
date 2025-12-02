# from collections import defaultdict
# class Solution(object):
#     def groupAnagrams(self, strs):
#         anagram_map = defaultdict(list)  #creates a hashtable

#         for word in strs:
#             key = tuple(sorted(word)) #converts each word in str to sorted tuple
#             anagram_map[key].append(word) #stores similar keys in a single list 


#         return list(anagram_map.values())

class Solution:
    def groupAnagrams(self, strs):
        ans = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            ans[key].append(s)
        
        return list(ans.values())
        