You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

  Complete the swap_case function in the editor below.

swap_case has the following parameters:

string s: the string to modify
Returns

string: the modified string
Input Format

A single line containing a string .

Constraints


Sample Input 0
  "Pythonist".

Sample Output 0
  "pYTHONIST".

def swap_case(s):
    value = s
    if len(s) > 0 and len(s) <= 1000:
        value = ''    
        for i in range(len(s)):
            value += s[i].capitalize() if s[i] == s[i].lower() else s[i].lower()
    return value
