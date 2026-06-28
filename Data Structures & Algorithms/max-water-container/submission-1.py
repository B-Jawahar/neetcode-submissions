class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        n=len(heights)
        right=n-1
        container=0
        while left<right:
            print((right-left)*min(heights[left],heights[right]))
            if container< ((right-left)*min(heights[left],heights[right])):
                container=((right-left)*min(heights[left],heights[right]))
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return container