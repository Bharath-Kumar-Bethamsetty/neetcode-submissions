from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashtable = defaultdict(list)

        for s in strs:
            alp = [0] * 26
            for ch in s:
                alp[ord(ch)-ord('a')] += 1
            hashtable[tuple(alp)].append(s)
        
        return list(hashtable.values())




        