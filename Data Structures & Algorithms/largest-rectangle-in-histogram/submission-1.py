class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)
        for i in range(len(heights)):
            start = i
            while stack and heights[i] < stack[-1][1]:
                index, value = stack.pop()
                max_area = max(max_area, (i-index)*value)
                if index < start:
                    start = index
            stack.append((start,heights[i]))
        return max_area