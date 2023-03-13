def anagrams(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

if __name__ == "__main__":
    print(anagrams("Heyho", "Hohey"))