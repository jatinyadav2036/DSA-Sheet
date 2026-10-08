class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda x: x[1])

        arrows = 0
        arrow_position = None

        for start, end in points:
            # Current arrow cannot burst this balloon
            if arrow_position is None or start > arrow_position:
                arrows += 1
                arrow_position = end

        return arrows