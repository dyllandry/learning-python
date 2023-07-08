def reverse(string):
    # You can't modify strings in Python, so instead treat
    # it as a list.
    reversed_chars = []
    for index in range(0, len(string)):
        char_index = len(string) - index - 1
        char = string[char_index]
        reversed_chars.append(char)
    return "".join(reversed_chars)

alphabet = "abcdefghijklmnopqrstuvwxyz"
reversed_alphabet = reverse(alphabet)

print(alphabet)
print(reversed_alphabet)
