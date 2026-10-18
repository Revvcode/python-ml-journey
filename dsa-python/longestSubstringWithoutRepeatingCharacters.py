class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Return the length of the longest substring without repeated characters.

        Sliding-window approach:
        - left marks the start of the current window.
        - last_seen stores the most recent index of each character.
        - If a character repeats inside the window, move left past its
          previous occurrence.
        """
        left = 0
        longest = 0
        last_seen = {}

        for right, char in enumerate(s):
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1

            last_seen[char] = right
            longest = max(longest, right - left + 1)

        return longest


if __name__ == "__main__":
    solution = Solution()
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3
    assert solution.lengthOfLongestSubstring("bbbbb") == 1
    assert solution.lengthOfLongestSubstring("pwwkew") == 3
    assert solution.lengthOfLongestSubstring("") == 0
    print("All test cases passed.")
