from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        # Frequency map for characters in t
        dict_t = Counter(t)
        required = len(dict_t)
        
        # Initialize the sliding window
        window_counts = defaultdict(int)
        l, r = 0, 0
        formed = 0
        min_length = float('inf')
        min_window = ""
        
        while r < len(s):
            char = s[r]
            window_counts[char] += 1
            
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1
            
            while l <= r and formed == required:
                char = s[l]
                
                # Update minimum window
                if r - l + 1 < min_length:
                    min_length = r - l + 1
                    min_window = s[l:r + 1]
                
                # Contract the window
                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1
                
                l += 1
            
            r += 1
        
        return min_window

solution = Solution()
print(solution.minWindow("ADOBECODEBANC", "ABC")) 
print(solution.minWindow("a", "a"))  
print(solution.minWindow("a", "aa"))  
