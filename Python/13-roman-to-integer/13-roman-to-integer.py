class Solution:
    def __init__(self, s: str):
        self.s = s

    def romanToInt(self):
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        result = 0
        for i in range(len(self.s)):
            curr_value = roman_dict[self.s[i]]
            next_value = roman_dict[self.s[i + 1]] if i + 1 < len(self.s) else 0

            if curr_value < next_value:
                result -= curr_value
            
            elif curr_value >= next_value:
                result += curr_value
        
        return result