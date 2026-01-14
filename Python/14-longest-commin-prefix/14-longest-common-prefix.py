class Solution:
    def __init__(self, strs: list[str]):
        self.strs = strs

    def longestCommonPrefix(self):
        if not self.strs:
            return ""
        
        prefix = self.strs[0]
        for st in self.strs[1:]:
            while prefix and not st.startswith(prefix):
                prefix = prefix[:-1]

            if not prefix:
                return ""
            
        return prefix
    
print(Solution(['flower', 'floor', 'slask']).longestCommonPrefix())