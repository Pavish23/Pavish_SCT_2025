#Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#You must write an algorithm that runs in O(n) time and without using the division operation.
#Example 1:

#Input: nums = [1,2,3,4]
#Output: [24,12,8,6]
#Example 2:
#Input: nums = [-1,1,0,-3,3]
#Output: [0,0,9,0,0]
#Constraints:

#2 <= nums.length <= 105
#-30 <= nums[i] <= 30
#The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        left_products, right_products, result = [1] * n, [1] * n, [1] * n

        left_product, right_product = 1, 1

        for i in range(n):

            left_products[i] = left_product

            right_products[n - 1 - i] = right_product

            left_product *= nums[i]

            right_product *= nums[n - 1 - i]

        for i in range(n):

            result[i] = left_products[i] * right_products[i]

        return result

# Example usage:

nums = [1, 2, 3, 4]

solution = Solution()

result = solution.productExceptSelf(nums)

print(result)
