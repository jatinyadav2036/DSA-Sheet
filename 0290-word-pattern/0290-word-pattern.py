class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()

        # Number of pattern characters must match number of words
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for char, word in zip(pattern, words):

            # Existing character must map to the same word
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False

            # Existing word must map to the same character
            if word in word_to_char:
                if word_to_char[word] != char:
                    return False

            # Create the mapping
            char_to_word[char] = word
            word_to_char[word] = char

        return True
