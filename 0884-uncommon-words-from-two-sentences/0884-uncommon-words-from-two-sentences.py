
class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        words = s1.split() + s2.split()

        freq = {}

        for word in words:
            freq[word] = freq.get(word, 0) + 1

        result = []

        for word in freq:
            if freq[word] == 1:
                result.append(word)

        return result
