class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # Edge case: if input is empty, return an empty list
        if not digits:
            return []
            
        # Telephone keypad mapping
        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }
        
        result = []
        
        def backtrack(index, current_combination):
            # Base case: if the combination is complete
            if index == len(digits):
                result.append("".join(current_combination))
                return
            
            # Get letters that the current digit maps to
            current_digit = digits[index]
            letters = phone_map[current_digit]
            
            # Loop through the letters and recurse
            for letter in letters:
                current_combination.append(letter)   # Choose
                backtrack(index + 1, current_combination) # Explore
                current_combination.pop()             # Unchoose (Backtrack)
                
        # Start the recursion from the first digit
        backtrack(0, [])
        return result
