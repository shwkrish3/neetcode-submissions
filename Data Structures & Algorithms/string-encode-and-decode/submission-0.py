class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            # Find the delimiter starting from position i
            j = s.find('#', i)
            
            # Extract the length of the upcoming string
            length = int(s[i:j])
            
            # Move index past the '#' delimiter
            i = j + 1
            
            # Extract the actual string using the length and append to results
            res.append(s[i : i + length])
            
            # Move index to the start of the next encoded block
            i += length
            
        return res
