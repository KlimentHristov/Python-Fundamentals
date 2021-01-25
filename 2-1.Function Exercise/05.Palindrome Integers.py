def is_palindrome(nums):
    return True if nums == nums[::-1] else False


numbers = input().split(', ')
mylist = list(numbers)

for i in mylist:
    print(is_palindrome(i))