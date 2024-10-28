
def is_palindrome(s):
    return s == s[::-1]




def main():
    print(is_palindrome("pyhton"))
    print(is_palindrome("ana"))

if __name__ == "__main__":
    main()
