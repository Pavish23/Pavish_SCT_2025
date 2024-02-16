#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#Example 1:

#Input: s = "anagram", t = "nagaram"
#Output: true
#Example 2:

#Input: s = "rat", t = "car"
#Output: false
 

#Constraints:

#1 <= s.length, t.length <= 5 * 104
#s and t consist of lowercase English letters.

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        # Initialize a dictionary to store the frequency of characters in the first string
        char_frequency = {}

        # Count the frequency of characters in the first string
        for char in s:
            char_frequency[char] = char_frequency.get(char, 0) + 1

        # Decrement the frequency of characters in the second string
        for char in t:
            if char not in char_frequency or char_frequency[char] == 0:
                return False
            char_frequency[char] -= 1

        # Check if all frequencies are zero
        return all(value == 0 for value in char_frequency.values())


        
