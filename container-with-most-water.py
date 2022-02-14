# container with most water
# https://leetcode.com/problems/container-with-most-water/
# the function maxArea -> take in a list of integers and return an integer
# 3 variables to keep track of the current max area, left and right pointers
# left pointer initialized to the first elements of the list
# right pointer initialized to the last elements of the list
# current max area initialized to 0
# height will be the lower of the two elements at the left and right pointers
# width will be the difference between the right pointer and left pointer
# compute the area between the 2 pointer and compare result with current max area, if result is greater than current max area, update current max area to result
# compare the height of the 2 pointer and shift the pointer that is shorter 
# [to compensate for the reduction in width, we want to move the pointer that is shorter to a taller line]
# recompute current max area

class Solution:
    def maxArea(self, height: list[int]) -> int:
        current_max_area = 0
        left = 0
        right = len(height)-1
        
        while (left < right):
            area = (right - left) * min(height[left], height[right])
            if area > current_max_area:
                current_max_area = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return current_max_area

a = [1,8,6,2,5,4,8,3,7]
sol = Solution()
print(sol.maxArea(a))
