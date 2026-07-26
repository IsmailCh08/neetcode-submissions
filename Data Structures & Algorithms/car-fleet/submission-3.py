class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = sorted(zip(position,speed), reverse=True)
        for position,speed in cars:
            if stack and (target-position) / speed <= stack[-1]:
                continue
            else:
                stack.append((target-position) / speed)
        return len(stack)