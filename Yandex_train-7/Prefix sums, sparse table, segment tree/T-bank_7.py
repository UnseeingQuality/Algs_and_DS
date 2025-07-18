def is_valid(word):
    n = len(word)
    for i in range(n):
        for j in range(i + 2, n):
            if word[i] == word[j]:
                between = word[i + 1:j]
                for a in range(len(between)):
                    for b in range(a + 1, len(between)):
                        if between[a] == between[b] and between[a] != word[i]:
                            return False
    return True


def backtrack(word, alphabet, max_len, results):
    if len(word) > max_len[0]:
        max_len[0] = len(word)
        results.clear()
        results.add("".join(word))
    elif len(word) == max_len[0]:
        results.add("".join(word))

    for c in alphabet:
        word.append(c)
        if is_valid(word):
            backtrack(word, alphabet, max_len, results)
        word.pop()


alphabet = [str(i) for i in range(10)]
results = set()
max_len = [0]
backtrack([], alphabet, max_len, results)

print(f"Максимальная длина: {max_len[0]}")
print(f"Количество слов: {len(results)}")
