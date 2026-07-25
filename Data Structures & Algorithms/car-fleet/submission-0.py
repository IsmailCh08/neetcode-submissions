class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = sorted(zip(position, speed), reverse=True)
        for position, speed in cars:
            time = (target - position) / speed
            if stack and time > stack[-1]:
                stack.append(time)
            elif not stack:
                stack.append(time)
            else:
                continue
        return len(stack)