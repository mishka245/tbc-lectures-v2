def is_palindrome(s):
    for i in range(0, len(s)//2):
        if s[i] != s[(-1) * i - 1]:
            return False
    return True




def main():
    print(is_palindrome("pyhton"))
    print(is_palindrome("ana"))

if __name__ == "__main__":
    main()
