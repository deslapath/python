
def  single_root_words(root_word, *other_words):
    same_words = []
    root_word_lower = root_word.lower()
    other_words_lower = [item.lower() for item in other_words]
    for word_lower in other_words_lower:
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word_lower)
    return same_words

result1 = single_root_words('лист', 'лиса', 'листВЕНница', 'листочек', 'Полипает', 'четверолистник')
print(result1)
result2 = single_root_words('круг', 'Закругленная', 'скрипка', 'крУгОвАя')
print(result2)