#Given a string s, find the length of the longestsubstring without repeating characters.
#Example 1:

#Input: s = "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3.
#Example 2:
#Input: s = "bbbbb"
#Output: 1
#Explanation: The answer is "b", with the length of 1.
#Example 3:

#Input: s = "pwwkew"
#Output: 3
#Explanation: The answer is "wke", with the length of 3.
#Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#Constraints:

#0 <= s.length <= 5 * 104
#s consists of English letters, digits, symbols and spaces.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
           return 0

        length = 0
        index= {}
        start = 0

        for i in range(len(s)):
            if s[i] in index:
              start = max(start, index[s[i]] + 1)
            index[s[i]] = i
            length = max(length, i - start + 1)

        return length

c=Solution()
s1 = "abcabcbb"
print(c.lengthOfLongestSubstring(s1)) 

s2 = "bbbbb"
print(c.lengthOfLongestSubstring(s2))  

s3 = "pwwkew"
print(c.lengthOfLongestSubstring(s3))
