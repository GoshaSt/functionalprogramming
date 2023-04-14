def count_words(resume):
    word_count = len(resume.split())
    return word_count

def print_resume(resume):
    print(resume)


resume = "Я Статенин Георгий, учусь в SU."
word_count = count_words(resume)
test = print_resume(resume)
print(test)
print(f"Количество слов: {word_count}")
