
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        from collections import Counter

        # Count only letters, ignoring digits, spaces, and case
        required = Counter(
            ch.lower() for ch in licensePlate if ch.isalpha()
        )

        result = ""

        for word in words:
            counts = Counter(word)

            # Check whether the word contains all required letters
            if all(counts[ch] >= required[ch] for ch in required):
                if result == "" or len(word) < len(result):
                    result = word

        return result
