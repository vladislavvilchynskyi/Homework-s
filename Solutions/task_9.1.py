def popular_words (text, words):
    text = text.lower()
    words_list = text.split()
    words_count = {word: 0 for word in words}

    for word in words_list:
        if word in words_count:
            words_count[word] += 1

    return words_count
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
