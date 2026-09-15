class Solution:
    def longestPalindrome(self, s: str) -> str:
        # s[i:j] is a palindrome only if P(s[i+1:j-1]) and s[i] == s[j]

        max_length = 1
        start_index = 0

        def expand_at_centre(s, start, end):
            left = start
            right = end
            palindrome_length = 0
            while left >=0 and right<len(s):
                if s[left] == s[right]:
                    palindrome_length += 2
                    left -= 1
                    right += 1
                else:
                    break
            if start == end:
                # account for same character at center
                palindrome_length -= 1

            return palindrome_length, left+1

        for i in range(len(s)):
            odd_len, odd_start_char = expand_at_centre(s, i, i)
            even_len, even_start_char = expand_at_centre(s, i, i+1)

            if odd_len > max_length:
                max_length = odd_len
                start_index = odd_start_char
            
            if even_len > max_length:
                max_length = even_len
                start_index = even_start_char
        
        return s[start_index:start_index+max_length]