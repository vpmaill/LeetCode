def lenghtOfLastWord(s):
    return len(s.strip().split()[-1])


print(lenghtOfLastWord("   fly me   to   the moon  "))
