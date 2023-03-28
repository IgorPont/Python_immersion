text = 'Отличительным аспектом статьи является её готовность. Если подготавливаемый материал так и ' \
       'не был опубликован (не вышел в тираж, не получил распространения), то такой труд относить ' \
       'к статье некорректно.'

# Первый способ
count_char = {}
for i in text:
    if i not in count_char:
        count_char[i] = 1
    else:
        count_char[i] += 1
print(count_char)

# Второй способ
count_char2 = {}
for i in text:
    count_char2[i] = text.count(i)
print(count_char2)
