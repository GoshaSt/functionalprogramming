import string

STOP_WORDS = {
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'have', 'in', 'is', 'it',
    'its', 'of', 'on', 'that', 'the', 'to', 'was', 'were', 'will', 'with'
}

def read_text_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def count_words(words):
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

def process_text(text, num_most_common=10):
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    filtered_words = [word for word in words if word not in STOP_WORDS]
    word_counts = count_words(filtered_words)
    unique_words_count = len(set(filtered_words))
    return unique_words_count, sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:num_most_common]

filename = 'text_file.txt'
text = read_text_from_file(filename)

unique_words_count, most_common_words = process_text(text)
print(f'Количество уникальных слов после удаления стоп-слов: {unique_words_count}')
print(f'Самые часто встречающиеся слова в файле {filename}:')
for word, count in most_common_words:
    print(f'{word}: {count}')
