# Слова в тексте разбиваются в список, а далее разбиваются в словарь вида
# <n-ное слово в тексте>: <n + 1 -ное слово в тексте>
# То есть каждое значение хранит в себе вариацию тех слов, которые могут стоять за ним

f = open('orig_text.txt', mode='r', encoding='UTF-8')
data = f.read().split()
for i in range(len(data)):
    if not (data[i][-1].isalpha() or data[i][-1].isdigit()):
        if len(data[i][:-1]) >= 1:
            data[i] = data[i][:-1].lower()
    else:
        data[i] = data[i].lower()
ans = set(data)
a = {}
for elem in ans:
    indices = [data[i + 1] for i in range(len(data) - 1) if data[i] == elem]
    a[elem] = indices