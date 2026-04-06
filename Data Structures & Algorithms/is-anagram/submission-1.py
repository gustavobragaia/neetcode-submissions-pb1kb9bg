class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create dict for hashmap
        frequency = dict()

        # primary check
        if len(s) != len(t): return False

        # add each letter into the hashmap
        for i in s:
            frequency[i] = frequency.get(i, 0) + 1
        
        # need to check in j is on map
        for j in t:
            # letter isnt on map
            if j not in frequency:
                return False
            # if is on map, subtract
            frequency[j] -= 1
            
            # if letter of j appear more times than i (on s)
            if frequency[j] < 0:
                return False
        return True
            