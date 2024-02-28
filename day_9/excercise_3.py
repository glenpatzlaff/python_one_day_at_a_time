def analyze_text(text):
    words = text.lower().split()
    unique_words = set(words)
    word_count = len(words)
    unique_word_count = len(unique_words)
    word_frequency = {word: words.count(word) for word in unique_words}

    return word_count, unique_word_count, word_frequency


sentence = "The quick brown fox jumps over the lazy dog. The dog was not amused."
word_count, unique_word_count, word_frequency = analyze_text(sentence)
print(f"Word Count: {word_count}\nUnique Word Count: {unique_word_count}\nWord Frequency: {word_frequency}")
