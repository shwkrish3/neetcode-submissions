class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Create a character count array for 'a' through 'z'
            count = [0] * 26
            
            for char in s:
                # Map character to index 0-25 using ASCII values
                count[ord(char) - ord('a')] += 1
                
            # Convert mutable list to immutable tuple to use as dictionary key
            anagram_map[tuple(count)].append(s)
            
        # Return all grouped anagram lists
        return list(anagram_map.values())
        