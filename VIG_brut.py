import enchant

def vigenere_decrypt(ciphertext, key):
    # Create a mapping of the alphabet to the shifted alphabet
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key_len = len(key)
    key_int = [ord(i) for i in key]
    plaintext = ""

    for i, c in enumerate(ciphertext.upper()):
        if c in alphabet:
            plaintext += alphabet[(alphabet.index(c) - key_int[i % key_len]) % 26]
        else:
            plaintext += c

    return plaintext

def brute_force_keyword(ciphertext):
    # Initialize the dictionary
    dictionary = enchant.Dict("en_US")

    # Try all possible keywords
    for i in range(1, 26):
        keyword = "A" * i
        for j in range(26 ** i):
            # Decrypt the ciphertext with the current keyword
            plaintext = vigenere_decrypt(ciphertext, keyword)

            # Check if the plaintext is in English
            if all(dictionary.check(word) for word in plaintext.split()):
                print(f"Keyword found: {keyword}")
                print(f"Plaintext: {plaintext}")
                return

            # Increment the keyword
            keyword = increment_keyword(keyword)

def increment_keyword(keyword):
    # Increment the keyword by one
    keyword_int = [ord(c) for c in keyword]
    keyword_int[-1] += 1
    keyword = "".join([chr(c) for c in keyword_int])
    if "Z" in keyword:
        keyword = increment_keyword(keyword.replace("Z", "A", 1))
    return keyword

# Get user input for the ciphertext
ciphertext = input("Enter the ciphertext: ")

# Brute force the keyword
brute_force_keyword(ciphertext)
