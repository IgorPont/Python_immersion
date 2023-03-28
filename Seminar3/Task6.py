text = 'Enter some txt: Hellow world'
max_len = max(len(w) for w in text.split())

for i, item in enumerate(sorted(text.split()), start=1):
    print(f'{i} {item :>{max_len}}')
