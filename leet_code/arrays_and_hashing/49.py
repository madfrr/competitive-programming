#49. Group Anagrams - https://leetcode.com/problems/group-anagrams/description/

'''
Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]

'''
from typing import List
class Solution:
    def hash(self, word):
        aux = 0
        for w in word:
            aux += ord(w)
        
        return str(aux)
    
    def check_anagram(self, w1: str, w2: str):
        frequent_str_1 = {}
        for n in w1:
            frequent_str_1[n] = frequent_str_1.get(n, 0) + 1
        frequent_str_2 = {}
        for n in w2:
            frequent_str_2[n] = frequent_str_2.get(n, 0) + 1
        
        return frequent_str_2 == frequent_str_1

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # each word anagram must have the same hash, but not every equal hash means that the word is anagram
        anagrams = {}
        for s in strs:
            h = self.hash(s)
            if h not in anagrams:
                anagrams[h] = [s]
                continue
            
            # check if is an anagram, if it's true -> append word in the list
            word = anagrams[h][0]
            if self.check_anagram(s, word):
                anagrams[h].append(s)
            else:  # check if is an anagram, if it's false -> check if have another list and check anagrams
                # create another key in anagrams dic
                # check if this key exists
                h += '_'
                flag = True
                while h in anagrams:
                    word = anagrams[h][0]
                    if self.check_anagram(s, word):
                        anagrams[h].append(s)
                        flag = False
                        break
                    h += '_'
                
                if flag:
                    anagrams[h] = [s]

        return list(anagrams.values())
    
    '''
    sol 2 -> vi no site ;-;
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())
    '''
    

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(Solution().groupAnagrams([""]))
print(Solution().groupAnagrams(["a"]))