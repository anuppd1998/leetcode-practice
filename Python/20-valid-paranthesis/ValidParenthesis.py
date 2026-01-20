class ValidParenthesis:
    """
    Solution for LeetCode 20: Valid Parentheses.
    The goal is to determine if the input string has validly closed and nested brackets.
    """

    def __init__(self, s: str):
        """
        Initialize with the string to be validated.
        :param s: String containing only '(', ')', '{', '}', '[' and ']'
        """
        self.s = s

    def isValid(self) -> bool:
        """
        Validates parentheses using a stack-based approach.
        Time Complexity: O(n) - where n is the length of the string.
        Space Complexity: O(n) - in the worst case where all characters are openers.
        """
        # Mapping opening brackets to their required closing counterparts
        parenthesis_dict = {"(": ")", "{": "}", "[": "]"}
        
        # Stack to store opening brackets
        check_list = []

        # Early exit for empty strings or strings starting with a closing bracket
        if not self.s or self.s[0] in parenthesis_dict.values():
            return False
        
        for paren in self.s:
            # If current character is an opening bracket, push to stack
            if paren in parenthesis_dict:
                check_list.append(paren)
            
            # If current character is a closing bracket
            else:
                # If stack is empty, we have a closer without a preceding opener
                if not check_list:
                    return False
                
                # Pop the last opener and check if it matches the current closer
                popped_item = check_list.pop()
                if parenthesis_dict[popped_item] != paren:
                    return False
        
        # If the stack is empty, all parentheses were matched correctly
        return len(check_list) == 0
    
test_cases = ["()[]{}", "([)]", "{[]}", "((", "]]"]
    
for case in test_cases:
    vp = ValidParenthesis(case)
    print(f"Input: {case} -> Is Valid: {vp.isValid()}")
