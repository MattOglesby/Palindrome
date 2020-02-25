#!/usr/bin/env python3

class Palindrome:
    def __init__(self, p):
        try:
            self.p = p.lower()
        except AttributeError:
            print("Please only include letters in the input")
        finally:
            pass
    def reverse(self):
        # Returns a reversed string
        return self.p[::-1]
    def isPalindrome(self):
        try:
            if self.p == self.reverse():
                print("The word " + self.p + " is a palindrome: " + self.reverse())
            else:
                print("The word " + self.p + " is not a palindrome: " + self.reverse())
        except AttributeError:
            print("Something's wrong with the data type for input variable or the data type doesn't exist")
            return


if __name__ == "__main__":
    word1 = "iamottomai"
    word2 = "himynameisbob"
    word3 = 653218
    word4 = "cattottac"
    test1 = Palindrome(word1)
    test1.isPalindrome()
    test2 = Palindrome(word2)
    test2.isPalindrome()
    test3 = Palindrome(word3)
    test3.isPalindrome()
    test4 = Palindrome(word4)
    test4.isPalindrome()
