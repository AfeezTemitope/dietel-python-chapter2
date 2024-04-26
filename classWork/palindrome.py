def palindrome_test(String):
    for character in range(len(String) - 1, -1, -1):
        if String[character] == String[len(String) - 1 - character]:
            return True
        else:
            return False
