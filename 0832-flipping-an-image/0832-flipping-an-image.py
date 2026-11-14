
class Solution(object):
    def flipAndInvertImage(self, image):
        for row in image:
            left = 0
            right = len(row) - 1

            while left <= right:
                row[left], row[right] = 1 - row[right], 1 - row[left]

                left += 1
                right -= 1

        return image
