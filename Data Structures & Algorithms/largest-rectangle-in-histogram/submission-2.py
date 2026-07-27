class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)
        for i,height in enumerate(heights):
            start = i
            while stack and height < stack[-1][1]:
                index, stack_height = stack.pop()
                max_area = max(max_area, (i - index) * stack_height)
                if index < start:
                    start = index
            else:
                stack.append((start,height))
        return max_area