class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        inv = 0
        x_copy = x
        while x > 0:
            inv = inv * 10 + x % 10
            x = int(x / 10)

        if inv == x_copy:
            return True
        else:
            return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(Solution().isPalindrome(121))

