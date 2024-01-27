from typing import List
import re
import collections


class Solution:
    def most_common_word(self, paragraph: str, banned: List[str]) -> str:
        # lower case, frequent, not banned
        paragraph = paragraph.lower()
        paragraph = re.sub(r"([!?',;.\s])", " ", paragraph)

        counter_map = {}
        for word in paragraph.split():
            if word in banned:
                continue

            if word not in counter_map:
                counter_map[word] = 1
            else:
                counter_map[word] += 1

        max_key = ""
        max_value = 0
        for key, value in counter_map.items():
            if value > max_value:
                max_value = value
                max_key = key

        return max_key

    def most_common_word_2(self, paragraph: str, banned: List[str]):
        words = [word for word in re.sub(r"[^\w]", " ", paragraph).lower().split() if word not in banned]
        counts = collections.Counter(words)

        return counts.most_common(1)[0][0]


s = Solution()
result = s.most_common_word("Bob. hIt, baLl", ["hit", "bob"])
result2 = s.most_common_word_2("Bob. hIt, baLl", ["hit", "bob"])
print(result2)
