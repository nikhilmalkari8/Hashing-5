def isAlienSorted(words, order):
    # Step 1: Create a rank map for the alien language
    rank = {char: i for i, char in enumerate(order)}

    # Step 2: Compare adjacent words
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        
        # Compare characters of the two words
        for char1, char2 in zip(word1, word2):
            if rank[char1] < rank[char2]:
                break  # word1 < word2; valid order
            elif rank[char1] > rank[char2]:
                return False  # Invalid order
        else:
            # If we exhaust the characters and words are identical but lengths differ
            if len(word1) > len(word2):
                return False

    return True  # All comparisons passed

