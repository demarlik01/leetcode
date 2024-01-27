from collections import deque
import re

class Solution:
    def is_palindrome(self, s: str) -> bool:
        deq = deque()

        for char in s:
            if(char.isalnum()):
                deq.append(char.lower())

        while(len(deq) > 1):
            front_value = deq.pop()
            end_value = deq.popleft()
            if (front_value != end_value):
                return False
        return True
    
    def is_palindrome_2(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]
