from typing import List
import math


class Solution:
    def reverse_string(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        j = len(s) - 1
        for i in range(0, math.ceil((len(s) - 1) / 2)):
            s[i], s[j] = s[j], s[i]
            j -= 1


s = Solution()
s.reverse_string(["h", "e", "l", "l", "o"])
