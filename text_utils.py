def clean_text(text):
    text = text.lower()
    text = remove_punctuation(text)
    return text

def remove_punctuation(text):
    chars = ".,!?;:()\"'"
    for c in chars:
        text = text.replace(c, "")
    return text

def count_words(text):
    words = split_words(text)
    return len(words)

def split_words(text):
    return text.split()

def count_unique_words(text):
    words = split_words(text)
    return len(set(words))

def summarize_text(text):
    text = clean_text(text)
    word_count = count_words(text)
    unique_count = count_unique_words(text)
    return {
        "words": word_count,
        "unique_words": unique_count
    }