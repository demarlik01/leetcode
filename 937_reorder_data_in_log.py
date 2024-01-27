from typing import List


class Solution:
    def reorder_log_files(self, logs: List[str]) -> List[str]:
        # digit / leeter -> letter 먼저, letter는 lexicorgraphically, 사전적으로 같으면 identifier, digit은 순서 그대로
        digit_logs = []
        letter_logs = []

        for log in logs:
            first_value = log.split(" ", 1)[1][0]
            if first_value.isnumeric():
                digit_logs.append(log)
            else:
                letter_logs.append(log)

        letter_logs.sort(key=lambda x: (x.split(" ", 1)[1], x.split(" ", 1)[0]))

        return letter_logs + digit_logs

"""
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
"""
s = Solution()
result = s.reorder_log_files(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"])
print(result)
