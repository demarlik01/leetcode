import collections
from typing import List, Dict


class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = collections.defaultdict(list)
        for _str in strs:
            sorted_str = ''.join(sorted(_str))
            str_dict[sorted_str].append(_str)
        return str_dict.values()
